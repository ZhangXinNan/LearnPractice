def restore_model_ckpt(ckpt_file_path):
    sess = tf.Session()
 
    # 《《《 加载模型结构 》》》
    saver = tf.train.import_meta_graph('./ckpt/model.ckpt.meta') 
    # 只需要指定目录就可以恢复所有变量信息 
    saver.restore(sess, tf.train.latest_checkpoint('./ckpt'))  

    # 直接获取保存的变量
    print(sess.run('b:0'))

    # 获取placeholder变量
    input_x = sess.graph.get_tensor_by_name('x:0')
    input_y = sess.graph.get_tensor_by_name('y:0')
    # 获取需要进行计算的operator
    op = sess.graph.get_tensor_by_name('op_to_store:0')

    # 加入新的操作
    add_on_op = tf.multiply(op, 2)

    ret = sess.run(add_on_op, {input_x: 5, input_y: 5})
    print(ret) 