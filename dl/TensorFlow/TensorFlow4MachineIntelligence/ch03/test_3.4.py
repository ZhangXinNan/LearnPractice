#encoding=utf8
# 导入tensorflow库
import tensorflow as tf

# 显示创建一个Graph对象加以使用
graph = tf.Graph()

with graph.as_default():
    with tf.name_scope('variables'):
        global_step = tf.Variable(0, dtype=tf.int32, trainable=False, name='global_step')
        total_output = tf.Variable(0.0, dtype=tf.float32, trainable=False, name='total_output')
    with tf.name_scope('transformation'):
        with tf.name_scope("input"):
            a = tf.placeholder(tf.float32, shape=[None], name='input_placeholder_a')
        with tf.name_scope('intermediate_layer'):
            b = tf.reduce_prod(a, name='product_b')
            c = tf.reduce_sum(a, name='sum_c')
        with tf.name_scope('output'):
            output = tf.add(b, c, name='output')
    with tf.name_scope('update'):
        update_total = total_output.assign_add(output)
        increment_step = global_step.assign_add(1)
    with tf.name_scope('summaries'):
        avg = tf.div(update_total, tf.cast(increment_step, tf.float32), name='average')
        # tf.scalar_summary(b'Output', output, name='output_summary')
        # tf.scalar_summary(b'Sum of outputs over time', update_total, name='total_summary')
        # tf.scalar_summary(b'average of outputs over time', avg, name='average_summary')
        tf.summary.scalar(b'Output', output)
        tf.summary.scalar(b'Sum of outputs over time', update_total)
        tf.summary.scalar(b'average of outputs over time', avg)
    
    with tf.name_scope('global_ops'):
        init = tf.initialize_all_variables()
        # merged_summaries = tf.merge_all_summaries()
        merged_summaries = tf.summary.merge_all()


sess = tf.Session(graph=graph)
writer = tf.summary.FileWriter('./improved_graph', graph)
sess.run(init)

def run_graph(input_tensor):
    feed_dict = {a: input_tensor}
    _, step, summary = sess.run([output, increment_step, merged_summaries], feed_dict=feed_dict)
    writer.add_summary(summary, global_step=step)

run_graph([2, 8])
run_graph([3,1,3,3])
run_graph([8])
run_graph([1,2,3])
run_graph([11,4])
run_graph([4,1])
run_graph([7,3,1])
run_graph([6,3])
run_graph([0,2])
run_graph([4,5,6])

writer.flush()

writer.close()
sess.close()
