import os
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

img_dir = '/Users/zhangxin/data_public/ocr/icdar2015/4.1/ch4_test_images'


def get_img_file_list(img_dir):
    imgfile_list = []
    for filename in os.listdir(img_dir):
        if filename[0] == '.':
            continue
        img_path = os.path.join(img_dir, filename)
        imgfile_list.append(img_path)
    return imgfile_list

def picture_read():
    # 1 构造文件队列
    imgfile_list = get_img_file_list(img_dir)
    file_queue = tf.train.string_input_producer(imgfile_list)

    # 2 读取和解码
    ## 2.1 读取
    reader = tf.WholeFileReader()
    key, value = reader.read(file_queue)
    print(key, value)
    ## 2.2 解码
    image = tf.image.decode_jpeg(value)
    print("image: ", image)
    ## 2.3 图像预处理
    image_resized = tf.image.resize(image, (200, 200))
    image_resized.set_shape(shape=[200, 200, 3])
    print("image_resized : ", image_resized)

    # 3 批处理
    image_batch = tf.train.batch([image_resized], batch_size=100, num_threads=1, capacity=100)
    print("image_batch", image_batch)

    # 4 开启会话
    with tf.Session() as sess:
        # 【重要】开启线程
        coord = tf.train.Coordinator()
        threads = tf.train.start_queue_runners(sess=sess, coord=coord)

        k, v, im = sess.run([key, value, image_resized])
        print(k, im)

        # 回收线程
        coord.request_stop()
        coord.join(threads)
    pass


if __name__ == '__main__':
    # main()
    picture_read()
