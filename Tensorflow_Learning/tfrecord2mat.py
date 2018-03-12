# coding:utf-8 
'''
created on 2018/3/2

@author:sunyihuan
'''
import tensorflow as tf
import scipy.io as scio


def read_and_decode(filename):
    filename_queue = tf.train.string_input_producer([filename])
    read = tf.TFRecordReader()
    _, example = read.read(filename_queue)
    features = tf.parse_single_example(example,
                                       features={"label": tf.FixedLenFeature([], tf.int64),
                                                 "image_raw": tf.FixedLenFeature([], tf.string),
                                                 })
    img = tf.decode_raw(features["image_raw"], tf.uint8)
    print(img.get_shape)
    img = tf.reshape(img, [64, 64, 3])
    print(img.get_shape)
    # print(img.get_shape())
    img = tf.cast(img, tf.float32) * (1. / 255) - 0.5
    label = tf.cast(features['label'], tf.int32)

    return img, label


filename = "train.tfrecords"
img, label = read_and_decode(filename)
with tf.Session() as sess:
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(sess=sess, coord=coord)
    # coord = tf.train.CheckpointSaverHook
    img, label = sess.run([img, label])
    coord.request_stop()
    coord.join(threads)

print(img.shape, label.shape)
