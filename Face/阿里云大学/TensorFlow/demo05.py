
import tensorflow as tf
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
print(tf.__version__)


def graph_demo():
    print('查看图：')
    a = tf.constant(2)
    b = tf.constant(3)
    c = a + b
    # print("TensorFlow加法运算：\n", c)

    print("方法1：调用方法")
    default_g = tf.get_default_graph()
    print("default_g: ", default_g)

    print("方法2：查看属性")
    print("a的图属性：", a.graph)
    print("c的图属性：", c.graph)

    # 开启会话
    with tf.Session() as sess:
        c_value = sess.run(c)
        print("c_value : ", c_value)
        print("sess的图属性：", sess.graph)
        tf.summary.FileWriter("./tmp/", graph=sess.graph)

    # 自定义图
    new_g = tf.Graph()
    with new_g.as_default():
        a_new = tf.constant(20)
        b_new = tf.constant(30)
        c_new = a_new + b_new
        print("c_new : ", c_new)
        print("c_new的图属性：", c_new.graph)
    
    with tf.Session(graph=new_g) as new_sess:
        c_new_value = new_sess.run(c_new)
        print("c_new_value: ", c_new_value)
        print("new_sess的图属性：", new_sess.graph)
    return None

if __name__ == '__main__':
    # tensorflow_demo()
    graph_demo()

