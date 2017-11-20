# 服务于TensorFlow模型
本教程将向您展示如何使用TensorFlow服务组件导出已训练的TensorFlow模型，并使用标准tensorflow_model_server进行服务。 如果您已经熟悉TensorFlow服务，并且想了解更多关于服务器内部部件的工作原理，请参阅TensorFlow服务高级教程。

本教程使用TensorFlow教程中介绍的简单的Softmax回归模型，用于手写图像（MNIST数据）分类。 如果您不知道TensorFlow或MNIST是什么，请参阅MNIST for ML初学者教程。

本教程的代码由两部分组成：
* 一个Python文件，mnist_saved_model.py，用于训练和导出模型。
* 一个C ++文件main.cc，它是标准的TensorFlow模型服务器，用于发现新的导出模型并运行gRPC服务来提供服务。

开始之前，请完成先决条件。

# 训练和导出TensorFlow模型

您可以在mnist_saved_model.py中看到，训练与MNIST For ML初学者教程中的相同。 TensorFlow图在TensorFlow会话中启动，输入张量（图像）为x，输出张量（Softmax分数）为y。

然后我们使用TensorFlow的SavedModelBuilder模块来导出模型。 SavedModelBuilder将经过训练的模型的“快照”保存到可靠的存储器中，以便稍后加载进行推理。

有关SavedModel格式的详细信息，请参阅SavedModel README.md上的文档。

从mnist_saved_model.py，以下是一个简短的代码片段，用于说明将模型保存到磁盘的一般过程。
```
from tensorflow.python.saved_model import builder as saved_model_builder
...
export_path_base = sys.argv[-1]
export_path = os.path.join(
      compat.as_bytes(export_path_base),
      compat.as_bytes(str(FLAGS.model_version)))
print 'Exporting trained model to', export_path
builder = saved_model_builder.SavedModelBuilder(export_path)
builder.add_meta_graph_and_variables(
      sess, [tag_constants.SERVING],
      signature_def_map={
           'predict_images':
               prediction_signature,
           signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY:
               classification_signature,
      },
      legacy_init_op=legacy_init_op)
builder.save()
```

