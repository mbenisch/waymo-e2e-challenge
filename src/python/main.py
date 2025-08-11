import torch
import tensorflow as tf
import pdb
from src.python.waymo_open_dataset.protos import vector_pb2, map_pb2

# Specify the path to your TFRecord file(s)
tfrecord_path = '/Users/mbenisch/Downloads/test_202504211836-202504220845.tfrecord-00000-of-00266'
dataset = tf.data.TFRecordDataset(tfrecord_path)
pdb.set_trace()

for record in dataset:
    example = tf.train.Example.FromString(record)
    print(example)
    break