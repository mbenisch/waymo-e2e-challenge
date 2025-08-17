import tensorflow as tf
import pdb
from src.python.waymo_open_dataset.protos import dataset_pb2 as open_dataset

from src.python.waymo_open_dataset.protos import end_to_end_driving_data_pb2 as wod_e2ed_pb2
from src.python.waymo_open_dataset.protos import end_to_end_driving_submission_pb2 as wod_e2ed_submission_pb2


tfrecord_path = '/Users/mbenisch/Downloads/training_202504031202_202504151040.tfrecord-00000-of-00263'
dataset = tf.data.TFRecordDataset(tfrecord_path)
dataset_iter = dataset.as_numpy_iterator()
bytes_example = next(dataset_iter)
data = wod_e2ed_pb2.E2EDFrame()
data.ParseFromString(bytes_example)
pdb.set_trace()