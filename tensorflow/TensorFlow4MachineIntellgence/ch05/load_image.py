

import tensorflow as tf

sess = tf.InteractiveSession()
img_filename = '/Users/zhangxin/gitlab/dmocr/_tmp/anhp6880/0/*.jpg'
filename_queue = tf.train.string_input_producer(tf.train.match_filenames_once(img_filename))

image_reader = tf.WholeFileReader()
_, image_file = image_reader.read(filename_queue)
image = tf.image.decode_jpeg(image_file)
print image

sess.run(image)
