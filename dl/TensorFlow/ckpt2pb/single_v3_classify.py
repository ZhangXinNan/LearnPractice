# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import sys
import os
import numpy as np
import tensorflow as tf
import json
from sklearn.decomposition import PCA
from sklearn.externals import joblib


class ImageClassify:
    def __init__(self):
        self.model_file = "./v3/frozen_inception_v3.pb"
        self.label_file = "./porn_data/labels.txt"
        self.input_height = 299
        self.input_width = 299
        self.input_mean = 0
        self.input_std = 255.0
        self.input_layer = "input"
        self.output_layer = "InceptionV3/Predictions/Reshape_1"
        #self.feature_layer = "InceptionV3/Logits/Dropout_1b/Identity"
        self.top_k = 5
        self.step = 32

        self.graph = self.load_graph(self.model_file)
        self.labels = self.load_labels(self.label_file)

        self.input_name = "import/" + self.input_layer
        self.output_name = "import/" + self.output_layer

        self.input_operation = self.graph.get_operation_by_name(self.input_name);
        self.output_operation = self.graph.get_operation_by_name(self.output_name);


        self.sess = tf.Session(graph=self.graph)

        self.pro_input_name = "file_reader"
        self.pro_output_name = "normalized"
        self.pro_graph = self.load_pro_graph(input_height=self.input_height,
                                              input_width=self.input_width,
                                              input_mean=self.input_mean,
                                              input_std=self.input_std)
        self.pro_sess = tf.Session(graph = self.pro_graph)

    def load_labels(self,label_file):
        label = []
        proto_as_ascii_lines = tf.gfile.GFile(label_file).readlines()
        for l in proto_as_ascii_lines:
            label.append(l.rstrip())
        return label

    def load_graph(self,model_file):
        graph = tf.Graph()
        graph_def = tf.GraphDef()

        with open(model_file, "rb") as f:
            graph_def.ParseFromString(f.read())
        with graph.as_default():
            tf.import_graph_def(graph_def)
        return graph

    def load_pro_graph(self,input_height=299, input_width=299,
                    input_mean=0, input_std=255):
        graph = tf.Graph()
        with graph.as_default():
          file_name = tf.placeholder(tf.string,name = self.pro_input_name)
          file_reader = tf.read_file(file_name)
          image_reader = tf.image.decode_image(file_reader, channels = 3,name='pic_reader')
          float_caster = tf.cast(image_reader, tf.float32)
          dims_expander = tf.expand_dims(float_caster, 0);
          resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
          normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std],name = self.pro_output_name)

        return graph

    def read_tensor_from_image_file(self,file_name):
        result = self.pro_sess.run(self.pro_graph.get_operation_by_name(self.pro_output_name).outputs[0],
                     {self.pro_graph.get_operation_by_name(self.pro_input_name).outputs[0]:file_name})
        return result

    def predict_fromFile(self,image_path):
        t = self.read_tensor_from_image_file(image_path)
        results = self.sess.run(self.output_operation.outputs[0],
                      {self.input_operation.outputs[0]: t})
        results = np.squeeze(results)
        top_k = results.argsort()[-self.top_k:][::-1]
        res = []
        for i in top_k:
            res.append((self.labels[i], str(results[i])))
        return res


    def read_tensor_from_image_files(self,file_names, input_height=299, input_width=299,
                    input_mean=0, input_std=255):
        input_name = "file_reader"
        self.batch_pro_graph = tf.Graph()
        with self.batch_pro_graph.as_default() as g:
            filename_queue = tf.train.string_input_producer(file_names, num_epochs=None, shuffle=False)
            reader = tf.WholeFileReader()
            name,file_reader = reader.read(filename_queue)

            image_reader = tf.image.decode_jpeg(file_reader, channels = 3, name='jpeg_reader')
            float_caster = tf.cast(image_reader, tf.float32)
            dims_expander = tf.expand_dims(float_caster, 0);
            resized = tf.image.resize_bilinear(dims_expander, [input_height, input_width])
            normalized = tf.divide(tf.subtract(resized, [input_mean]), [input_std])
            final = tf.squeeze(normalized)

            #min_after_dequeue = 100
            #capacity = min_after_dequeue + 3 * self.step
            batch = tf.train.batch([final],batch_size=self.step)
            #batch = tf.train.batch([final],batch_size=self.step,capacity=capacity)
            with tf.Session(graph = g) as sess:
                sess.run(tf.local_variables_initializer())
                sess.run(tf.global_variables_initializer())
                coord = tf.train.Coordinator()
                threads = tf.train.start_queue_runners(coord=coord)
                result = sess.run([batch])
                coord.request_stop()
                coord.join(threads)
        return result[0]

    def predict_fromFiles(self,image_path):
        t = self.read_tensor_from_image_files(image_path,
                                  input_height=self.input_height,
                                  input_width=self.input_width,
                                  input_mean=self.input_mean,
                                  input_std=self.input_std)

        results = self.sess.run(self.output_operation.outputs[0],
                      {self.input_operation.outputs[0]: t})
        results = np.squeeze(results)
        res = []
        index = np.argsort(-results)
        for i,x in enumerate(index):
            single = []
            for j in x[:1]:
                single.append((self.labels[j], str(results[i][j])))
            res.append(single)

        return res

    def extract_fromFiles(self,image_path):
        t = self.read_tensor_from_image_files(image_path,
                                  input_height=self.input_height,
                                  input_width=self.input_width,
                                  input_mean=self.input_mean,
                                  input_std=self.input_std)

        results = self.sess.run(self.output_feature.outputs[0],
                      {self.input_operation.outputs[0]: t})
        results = np.squeeze(results)
        feas = self.pca.transform(results)
        return feas.tolist()

if __name__ == "__main__":
    classifier = ImageClassify()
    path = os.listdir("/data8/home/leiming1/data/test_data/data/")
    path = ["/data8/home/leiming1/data/test_data/data/" + v for v in path]
    for i, file_name in enumerate(path):
        result  = classifier.predict_fromFile(file_name)
        print(i, file_name, result[0])
        fp = open('./glm_test.txt', 'a')
        fp.write(file_name.split('/')[-1] + ',' + str(result[0][0]) + ',' + str(result[0][1]) + '\n')
        fp.close()
    sys.exit(0)
#    fea = classifier.extract_fromFile(file_name)
#    print (fea)

    result  = classifier.predict_fromFile(file_name)
    print (type(result),result)
    print (type(result[0]), result[0])
#    filenames = ['/data0/nfs_data/models/SlimInceptionV3/ImageClassify/test2.jpg','/data0/nfs_data/models/SlimInceptionV3/ImageClassify/test.jpg']
#    for i in range(10):
#        results = classifier.predict_fromFiles(filenames)
#        print (results)

#    feas = classifier.extract_fromFiles(filenames)
#    print (feas)
