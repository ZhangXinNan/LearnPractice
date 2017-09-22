#encoding=utf8
'''
Convert Images to TFRecords
'''
import os
import glob
import argparse
import tensorflow as tf

from itertools import groupby
from collections import defaultdict

IMAGE_SIZE = (28, 28)

def write_records_file(dataset, record_location, sess):
    """
    Fill a TFRecords file with the images found in `dataset` and include their category.

    Parameters
    ----------
    dataset : dict(list)
      Dictionary with each key being a label for the list of image filenames of its value.
    record_location : str
      Location to store the TFRecord output.
    """
    writer = None

    # Enumerating the dataset because the current index is used to breakup the files if they get over 100
    # images to avoid a slowdown in writing.
    current_index = 0
    for breed, images_filenames in dataset.items():
        for image_filename in images_filenames:
            if current_index % 100 == 0:
                if writer:
                    writer.close()

                record_filename = "{record_location}-{current_index}.tfrecords".format(
                    record_location=record_location,
                    current_index=current_index)
                print current_index, record_filename
                writer = tf.python_io.TFRecordWriter(record_filename)
            current_index += 1

            image_file = tf.read_file(image_filename)

            # In ImageNet dogs, there are a few images which TensorFlow doesn't recognize as JPEGs. This
            # try/catch will ignore those images.
            try:
                # image = tf.image.decode_jpeg(image_file)
                image = tf.image.decode_png(image_file)
            except:
                print(image_filename)
                continue

            # Converting to grayscale saves processing and memory but isn't required.
            # grayscale_image = tf.image.rgb_to_grayscale(image)
            # resized_image = tf.image.resize_images(grayscale_image, (250, 151))
            # resized_image = tf.image.resize_images(grayscale_image, IMAGE_SIZE)

            # tf.cast is used here because the resized images are floats but haven't been converted into
            # image floats where an RGB value is between [0,1).
            # image_bytes = sess.run(tf.cast(resized_image, tf.uint8)).tobytes()
            image_bytes = sess.run(tf.cast(image, tf.uint8)).tobytes()

            # Instead of using the label as a string, it'd be more efficient to turn it into either an
            # integer index or a one-hot encoded rank one tensor.
            # https://en.wikipedia.org/wiki/One-hot
            image_label = breed.encode("utf-8")

            example = tf.train.Example(features=tf.train.Features(feature={
                'label': tf.train.Feature(bytes_list=tf.train.BytesList(value=[image_label])),
                'image': tf.train.Feature(bytes_list=tf.train.BytesList(value=[image_bytes]))
            }))

            writer.write(example.SerializeToString())
    writer.close()



def load_image(image_filenames):
    training_dataset = defaultdict(list)
    testing_dataset = defaultdict(list)
    # Split up the filename into its breed and corresponding filename. The breed is found by taking the directory name
    image_filename_with_breed = map(lambda filename: (filename.split("/")[2], filename), image_filenames)
    # print image_filename_with_breed

    # Group each image by the breed which is the 0th element in the tuple returned above
    for dog_breed, breed_images in groupby(image_filename_with_breed, lambda x: x[0]):
        # Enumerate each breed's image and send ~20% of the images to a testing set
        for i, breed_image in enumerate(breed_images):
            if i % 5 == 0:
                testing_dataset[dog_breed].append(breed_image[1])
            else:
                training_dataset[dog_breed].append(breed_image[1])

        # Check that each breed includes at least 18% of the images for testing
        breed_training_count = len(training_dataset[dog_breed])
        breed_testing_count = len(testing_dataset[dog_breed])
        print dog_breed, breed_training_count, breed_testing_count
        assert round(float(breed_testing_count) / (breed_training_count + breed_testing_count), 2) > 0.18, "Not enough testing images."
    return training_dataset, testing_dataset

def png2tfrecord(sess):
    # image_filenames = glob.glob("./imagenet-dogs/n02*/*.jpg")
    image_filenames = glob.glob('./mnist/*/*.png')
    print len(image_filenames)

    training_dataset, testing_dataset = load_image(image_filenames)

    if not os.path.isdir('./output/testing-images'):
        os.makedirs('./output/testing-images')
    if not os.path.isdir('./output/training-images'):
        os.makedirs('./output/training-images')
    write_records_file(testing_dataset, "./output/testing-images/testing-image", sess)
    write_records_file(training_dataset, "./output/training-images/training-image", sess)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gpu', type=int, default=-1, help='if gpu < 0 , it will use cpu; else it will use gpu')
    return parser.parse_args()

def main(args):
    sess = tf.InteractiveSession()
    # png2tfrecord(sess)
    # ----------------
    # Load Images
    # --------------
    filename_queue = tf.train.string_input_producer(
        tf.train.match_filenames_once("./output/training-images/*.tfrecords"))
    reader = tf.TFRecordReader()
    _, serialized = reader.read(filename_queue)

    features = tf.parse_single_example(
        serialized,
        features={
            'label': tf.FixedLenFeature([], tf.string),
            'image': tf.FixedLenFeature([], tf.string),
        })

    record_image = tf.decode_raw(features['image'], tf.uint8)

    # Changing the image into this shape helps train and visualize the output by converting it to
    # be organized like an image.
    image = tf.reshape(record_image, [250, 151, 1])

    label = tf.cast(features['label'], tf.string)

    min_after_dequeue = 10
    batch_size = 3
    capacity = min_after_dequeue + 3 * batch_size
    image_batch, label_batch = tf.train.shuffle_batch(
        [image, label], batch_size=batch_size, capacity=capacity, min_after_dequeue=min_after_dequeue)


    # --------------
    # Model
    # --------------
    # Converting the images to a float of [0,1) to match the expected input to convolution2d
    float_image_batch = tf.image.convert_image_dtype(image_batch, tf.float32)

    conv2d_layer_one = tf.contrib.layers.convolution2d(
        float_image_batch,
        num_output_channels=32,     # The number of filters to generate
        kernel_size=(5,5),          # It's only the filter height and width.
        activation_fn=tf.nn.relu,
        weight_init=tf.random_normal,
        stride=(2, 2),
        trainable=True)
    pool_layer_one = tf.nn.max_pool(conv2d_layer_one,
        ksize=[1, 2, 2, 1],
        strides=[1, 2, 2, 1],
        padding='SAME')

    # Note, the first and last dimension of the convolution output hasn't changed but the
    # middle two dimensions have.
    print conv2d_layer_one.get_shape(), pool_layer_one.get_shape()

    conv2d_layer_two = tf.contrib.layers.convolution2d(
        pool_layer_one,
        num_output_channels=64,        # More output channels means an increase in the number of filters
        kernel_size=(5,5),
        activation_fn=tf.nn.relu,
        weight_init=tf.random_normal,
        stride=(1, 1),
        trainable=True)

    pool_layer_two = tf.nn.max_pool(conv2d_layer_two,
        ksize=[1, 2, 2, 1],
        strides=[1, 2, 2, 1],
        padding='SAME')

    print conv2d_layer_two.get_shape(), pool_layer_two.get_shape()
    
    flattened_layer_two = tf.reshape(
        pool_layer_two,
        [
            batch_size,  # Each image in the image_batch
            -1           # Every other dimension of the input
        ])

    print flattened_layer_two.get_shape()



    # The weight_init parameter can also accept a callable, a lambda is used here  returning a truncated normal
    # with a stddev specified.
    hidden_layer_three = tf.contrib.layers.fully_connected(
        flattened_layer_two,
        512,
        weight_init=lambda i, dtype: tf.truncated_normal([38912, 512], stddev=0.1),
        activation_fn=tf.nn.relu
    )

    # Dropout some of the neurons, reducing their importance in the model
    hidden_layer_three = tf.nn.dropout(hidden_layer_three, 0.1)

    # The output of this are all the connections between the previous layers and the 120 different dog breeds
    # available to train on.
    final_fully_connected = tf.contrib.layers.fully_connected(
        hidden_layer_three,
        120,  # Number of dog breeds in the ImageNet Dogs dataset
        weight_init=lambda i, dtype: tf.truncated_normal([512, 120], stddev=0.1)
    )

    # --------------
    # Training
    # --------------
    # Find every directory name in the imagenet-dogs directory (n02085620-Chihuahua, ...)
    # labels = list(map(lambda c: c.split("/")[-1], glob.glob("./imagenet-dogs/*")))
    labels = list(map(lambda c: c.split('/')[-1], glob.glob("./mnist/*")))

    # Match every label from label_batch and return the index where they exist in the list of classes
    train_labels = tf.map_fn(lambda l: tf.where(tf.equal(labels, l))[0,0:1][0], label_batch, dtype=tf.int64)

    # setup-only-ignore
    loss = tf.reduce_mean(
        tf.nn.sparse_softmax_cross_entropy_with_logits(
            final_fully_connected, train_labels))

    batch = tf.Variable(0)
    learning_rate = tf.train.exponential_decay(
        0.01,
        batch * 3,
        120,
        0.95,
        staircase=True)

    optimizer = tf.train.AdamOptimizer(
        learning_rate, 0.9).minimize(
        loss, global_step=batch)

    train_prediction = tf.nn.softmax(final_fully_connected)


    # # setup-only-ignore
    # filename_queue.close(cancel_pending_enqueues=True)
    # coord.request_stop()
    # coord.join(threads)
if __name__ == '__main__':
    main(get_args())


'''

'''