import tensorflow as tf

with tf.Session() as sess:
    with open('./graph.pb', 'rb') as f: 
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read()) 
        # output = tf.import_graph_def(graph_def, input_map={'input:0':40.}, return_elements=['out:0'], name='a') 
        # print(sess.run(output))

        # 在input_map那里可以替换为新的自定义的placeholder
        new_input = tf.placeholder(tf.float32, shape=())
        output = tf.import_graph_def(graph_def, input_map={'input:0':new_input}, return_elements=['out:0'], name='a') 
        print(sess.run(output, feed_dict={new_input:100}))