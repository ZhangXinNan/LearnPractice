
import tensorflow as tf

# (1) 准备数据
with tf.variable_scope("prepare_data"):
    X = tf.random_normal([100, 1])
    y_true = tf.matmul(X, [[0.8]]) + 0.7

# (2) 构造模型
with tf.variable_scope("create_model"):
    w = tf.Variable(initial_value=tf.random_normal(shape=[1, 1]))
    b = tf.Variable(initial_value=tf.random_normal(shape=[1, 1]))
    y_predict = tf.matmul(X, w) + b

# (3) 构造损失函数
with tf.variable_scope("loss_function"):
    error = tf.reduce_mean(tf.square(y_true-y_predict))

# (4) 优化损失
with tf.variable_scope("optimizer"):
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(error)

# 2 收集变量
tf.summary.scalar('error', error)
tf.summary.histogram("weights", w)
tf.summary.histogram("bias", b)
# 3 合并变量
merged = tf.summary.merge_all()

# 显示初始化变量
init = tf.global_variables_initializer()

# 5 开启会话
with tf.Session() as sess:
    sess.run(init)

    # 创建事件文件
    file_writer = tf.summary.FileWriter("./tmp/linear", graph=sess.graph)

    print('before training: w, b')
    print("\t", w, w.eval())
    print("\t", b, b.eval())

    # 开始训练
    for i in range(1000):
        sess.run(optimizer)
        summary = sess.run(merged)
        file_writer.add_summary(summary, i)
        if i % 100 == 0:
            # print(i, sess.run(error))
            print(i, error.eval())

    print('before training: w, b')
    print("\t", w, w.eval())
    print("\t", b, b.eval())
