# 运行slim下的例子报错：
```
device:GPU:0' because no supported kernel for GPU devices is available.
```

详细错误：
```
InvalidArgumentError (see above for traceback): Cannot assign a device for operation 'InceptionV3/Predictions/Softmax': Could not satisfy explicit device specification '/device:GPU:0' because no supported kernel for GPU devices is available.
Registered kernels:
  device='CPU'; T in [DT_HALF]
  device='CPU'; T in [DT_FLOAT]
  device='CPU'; T in [DT_DOUBLE]

         [[Node: InceptionV3/Predictions/Softmax = Softmax[T=DT_FLOAT, _device="/device:GPU:0"](InceptionV3/Predictions/Reshape)]]
```


1. 一种解决办法是：
```
config = tf.ConfigProto(allow_soft_placement = True)
sess = tf.Session(config = config)
```
但是我用的slim，没找到哪里改这个。

2. 另外找到一个：
I got the same problem. It is solved by changing the last few lines of codes defined in train_image_classifier.py
```
       ###########################
        # Kicks off the training. #
        ###########################
        
        session_config = tf.ConfigProto(allow_soft_placement=True)
        
        slim.learning.train(
                train_tensor,
                logdir=FLAGS.train_dir,
                master=FLAGS.master,
                is_chief=(FLAGS.task == 0),
                init_fn=_get_init_fn(),
                summary_op=summary_op,
                number_of_steps=FLAGS.max_number_of_steps,
                log_every_n_steps=FLAGS.log_every_n_steps,
                save_summaries_secs=FLAGS.save_summaries_secs,
                save_interval_secs=FLAGS.save_interval_secs,
                sync_optimizer=optimizer if FLAGS.sync_replicas else None,
                session_config=session_config,
                )
```


参考：
['InceptionV3/Predictions/Softmax': Could not satisfy explicit device specification '/device:GPU:0' #3118](https://github.com/tensorflow/models/issues/3118)

# 安装其他包
```
conda install -c conda-forge opencv
conda install -c conda-forge matplotlib
```