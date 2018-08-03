save_model2pb : [将TensorFlow的网络导出为单个文件](https://blog.csdn.net/encodets/article/details/54428456)

save_model2pb : [TensorFlow 保存模型为 PB 文件](https://zhuanlan.zhihu.com/p/32887066)

metaflow-ai/blog : [metaflow-ai/blog](https://github.com/metaflow-ai/blog/tree/master/tf-freeze)


[TensorFlow saving into/loading a graph from a file](https://stackoverflow.com/questions/38947658/tensorflow-saving-into-loading-a-graph-from-a-file)

1. CheckPoint文件（*.ckpt）
在训练TensorFlow模型时，每迭代若干轮就保存一次权值到磁盘，称为checkpoint。
只包含Variables对象序列化后的数据，不包含图结构。
由tf.train.Saver()对象调用saver.save()生成的。
载入checkpoint时，调用saver.restore(session, checkpoint_path)。

2. GraphDef(*.pb)
这种格式文件包含 protobuf 对象序列化后的数据，包含了计算图，可以从中得到所有运算符（operators）的细节，也包含张量（tensors）和 Variables 定义，但不包含 Variable 的值，因此只能从中恢复计算图，但一些训练的权值仍需要从 checkpoint 中恢复。
```python
def load_graph(model_file):
    graph = tf.Graph()
    graph_def = tf.GraphDef()

    with open(model_file, 'rb') as f:
        graph_def.ParseFromString(f.read())
    with graph.as_default():
        tf.import_graph_def(graph_def)
    return graph
```

3. SavedModel

