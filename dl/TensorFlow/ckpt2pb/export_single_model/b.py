import tensorflow as tf
with tf.Session() as sess:
    with open('./graph.pb', 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read()) 
        output = tf.import_graph_def(graph_def, return_elements=['out:0']) 
        print(sess.run(output))
