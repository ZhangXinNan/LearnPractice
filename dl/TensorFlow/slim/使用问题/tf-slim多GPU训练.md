

# 1 多GPU原理
* 模型并行：模型的不同部分在不同GPU上运行
* 数据并行：不同GPU上训练数据不同，但模型是同一个。Tensorflow支持的是数据并行。

数据并行的原理：CPU负责梯度平均和参数更新，在GPU上训练模型的副本。

多GPU并行计算的过程：
      1）模型副本定义在指定的GPU/CPU上;
      2）对于每一个GPU, 都是从CPU获得数据,前向传播进行计算,得到loss,并计算出梯度;
      3）CPU接到GPU的梯度,取平均值,然后进行梯度更新。

这个在tf的实现思路如下：
    模型参数保存在一个指定gpu/cpu上，模型参数的副本在不同gpu上，每次训练，提供batch_size*gpu_num数据，并等量拆分成多个batch，分别送入不同GPU。前向在不同gpu上进行，模型参数更新时，将多个GPU后向计算得到的梯度数据进行平均，并在指定GPU/CPU上利用梯度数据更新模型参数。假设有两个GPU（gpu0,gpu1），模型参数实际存放在cpu0上，实际一次训练过程如下图所示：



# 2 model_deploy.py文件及其用法
为了能让一个Slim模型在多个GPU上训练更加容易，这个模块提供了一系列帮助函数，比如create_clones()、optimize_clones()、deploy()、gather_clone_loss()、_add_gradients_summaries()、_sum_clones_gradients()等，该模块位于：https://github.com/tensorflow/models/blob/master/research/slim/deployment/model_deploy.py

详细步骤：
##（1）创建DeploymentConfig对象：config = model_deploy.DeploymentConfig(）
    Deployment类定义的源码如下：
```python
class DeploymentConfig(object):
   ''' 这个配置类描述了如何将一个模型部署在多个单机的多个GPU上，在每个单机上，模型将挥被复制num_clones次
   '''
  def __init__(self,num_clones=1, clone_on_cpu=False,
               replica_id=0, num_replicas=1,num_ps_tasks=0,
               worker_job_name='worker',ps_job_name='ps'):
 
    参数:
      num_clones : 每个单机部署多少个clone（即部署在多少个GPU）
      clone_on_cpu : 如果为True，则单机中的每个clone将被放在CPU中
      replica_id :   整数，模型所部署的单机的索引，通常是0.  
      num_replicas: 使用多少个单机，通常为1，表示单机部署。此时`worker_device`, `num_ps_tasks`和 `ps_device`这几个参数将被忽略。
      num_ps_tasks: ‘ps’作业(分布式作业)使用多少个单机，如果为0表示不使用单机
      worker_job_name: 默认为“worker”
      ps_job_name:默认为'ps'
 
    if num_replicas > 1:
      if num_ps_tasks < 1:
        raise ValueError('When using replicas num_ps_tasks must be positive')
    if num_replicas > 1 or num_ps_tasks > 0:
      if not worker_job_name:
        raise ValueError('Must specify worker_job_name when using replicas')
      if not ps_job_name:
        raise ValueError('Must specify ps_job_name when using parameter server')
    if replica_id >= num_replicas:
      raise ValueError('replica_id must be less than num_replicas')
    self._num_clones = num_clones
    self._clone_on_cpu = clone_on_cpu
    self._replica_id = replica_id
    self._num_replicas = num_replicas
    self._num_ps_tasks = num_ps_tasks
    self._ps_device = '/job:' + ps_job_name if num_ps_tasks > 0 else ''
    self._worker_device = '/job:' + worker_job_name if num_ps_tasks > 0 else ''
 
  @property
  def num_clones(self):
    return self._num_clones
  @property
  def clone_on_cpu(self):
    return self._clone_on_cpu
  @property
  def replica_id(self):
    return self._replica_id
  @property
  def num_replicas(self):
    return self._num_replicas
  @property
  def num_ps_tasks(self):
    return self._num_ps_tasks
  @property
  def ps_device(self):
    return self._ps_device
  @property
  def worker_device(self):
    return self._worker_device
 
  def caching_device(self):
    """缓存变量的设备    
    Returns:
      如果不需要被缓存则返回None，否则返回设备号
    """
    if self._num_ps_tasks > 0:
      return lambda op: op.device
    else:
      return None
 
  def clone_device(self, clone_index):
    """根据索引号返回用来创建克隆的设备号
    Args:
      clone_index: 克隆的索引值
    Returns:
       tf.device()的一个合适的值.
    """
    if clone_index >= self._num_clones:
      raise ValueError('clone_index must be less than num_clones')
    device = ''
    if self._num_ps_tasks > 0:
      device += self._worker_device
    if self._clone_on_cpu:
      device += '/device:CPU:0'
    else:
      device += '/device:GPU:%d' % clone_index
    return device
 
  def clone_scope(self, clone_index):
    """根据索引号返回所创建的克隆的scope名字
    Args:
      clone_index: 克隆的索引号
    Returns:
      tf.name_scope()的一个合适值.
    """
    if clone_index >= self._num_clones:
      raise ValueError('clone_index must be less than num_clones')
    scope = ''
    if self._num_clones > 1:
      scope = 'clone_%d' % clone_index
    return scope
 
  def optimizer_device(self):
    """模型参数更新的设备，单机时为CPU
    Returns:
      tf.device()的一个合适值
    """
    if self._num_ps_tasks > 0 or self._num_clones > 0:
      return self._worker_device + '/device:CPU:0'
    else:
      return ''
 
  def inputs_device(self):
    """建立输入的设备，即读取数据的设备，单机时为CPU
    Returns:
      tf.device()的一个合适值
    """
    device = ''
    if self._num_ps_tasks > 0:
      device += self._worker_device
    device += '/device:CPU:0'
    return device
 
  def variables_device(self):
    """创建模型变量的设备，单机时为CPU
    Returns:
      `tf.device()的一个合适值
    """
    device = ''
    if self._num_ps_tasks > 0:
      device += self._ps_device
    device += '/device:CPU:0'
 
    class _PSDeviceChooser(object):
      """Slim device chooser for variables when using PS."""
 
      def __init__(self, device, tasks):
        self._device = device
        self._tasks = tasks
        self._task = 0
 
      def choose(self, op):
        if op.device:
          return op.device
        node_def = op if isinstance(op, tf.NodeDef) else op.node_def
        if node_def.op.startswith('Variable'):
          t = self._task
          self._task = (self._task + 1) % self._tasks
          d = '%s/task:%d' % (self._device, t)
          return d
        else:
          return op.device
 
    if not self._num_ps_tasks:
      return device
    else:
      chooser = _PSDeviceChooser(device, self._num_ps_tasks)
      return chooser.choose

```



# 参考资料
[Slim模型部署多GPU](https://blog.csdn.net/MOU_IT/article/details/82759587)

作者：蓬莱道人 
来源：CSDN 
原文：https://blog.csdn.net/MOU_IT/article/details/82759587 
版权声明：本文为博主原创文章，转载请附上博文链接！
