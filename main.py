import numpy as np
import os
import sys
import tensorflow as tf

from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image
import cv2
import pre



def load_model(path):
  detection_graph = tf.compat.v1.Graph()
  with detection_graph.as_default():
    od_graph_def = tf.compat.v1.GraphDef()
    with tf.compat.v1.gfile.GFile(path, 'rb') as fid:
      serialized_graph = fid.read()
      od_graph_def.ParseFromString(serialized_graph)
      tf.import_graph_def(od_graph_def, name='')
  return detection_graph

#detection_graph = tf.compat.v1.Graph()
#with detection_graph.as_default():
#  od_graph_def = tf.compat.v1.GraphDef()
#  with tf.compat.v1.gfile.GFile(path, 'rb') as fid:
#    serialized_graph = fid.read()
#    od_graph_def.ParseFromString(serialized_graph)
#    tf.import_graph_def(od_graph_def, name='')

def load_image_into_numpy_array(image):
  (im_width, im_height) = image.size
  return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)


#img_path="G:/image/cat3.jpg"
#img_write="G:/image/temp.jpg"
#image = cv2.imread(img_path,1)
#img = pre.predict(image, detection_graph)
#cv2.imwrite(img_write,img)

def IMG(img_path,model_path,mst):
  image=cv2.imread(img_path,1)
  img=pre.predict(image,load_model(model_path),mst)
  img_write="G:/temp.jpg"
  cv2.imwrite(img_write,image)
  return img