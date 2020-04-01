import tensorflow as tf
import sys
from tensorflow.python.platform import gfile

from tensorflow.core.protobuf import saved_model_pb2
from tensorflow.python.util import compat
with tf.compat.v1.Session() as persisted_sess:
  print("load graph")
  with tf.compat.v1.gfile.FastGFile("Models/faster_rcnn_inception_v2_coco_2018_01_28/frozen_inference_graph.pb",'rb') as f:
    graph_def = tf.compat.v1.GraphDef()
    graph_def.ParseFromString(f.read())
    persisted_sess.graph.as_default()
    tf.import_graph_def(graph_def, name='')
    writer = tf.compat.v1.summary.FileWriter("./tf_summary", graph=persisted_sess.graph)

output_layer = 'loss:0'
input_node = 'Placeholder:0'

with tf.compat.v1.Session() as sess:
    input_tensor_shape = sess.graph.get_tensor_by_name('Placeholder:0').shape.as_list()
network_input_size = input_tensor_shape[1]

with tf.compat.v1.Session() as sess:
  try:
    prob_tensor = sess.graph.get_tensor_by_name(output_layer)
    predictions, = sess.run(prob_tensor, {input_node: [img]})
  except KeyError:
    print("Couldn't find classification output layer: " + output_layer + ".")
    print("Verify this a model exported from an Object Detection project.")
    exit(-1)