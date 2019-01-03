
# 问题
```
Exception in thread Thread-12:
Traceback (most recent call last):
  File "/home/work/anaconda3/envs/py36_tf/lib/python3.6/threading.py", line 916, in _bootstrap_inner
    self.run()
  File "/home/work/anaconda3/envs/py36_tf/lib/python3.6/threading.py", line 864, in run
    self._target(*self._args, **self._kwargs)
  File "build_imagenet_data_nobox.py", line 395, in _process_image_files_batch
    height, width)
  File "build_imagenet_data_nobox.py", line 213, in _convert_to_example
    'image/colorspace': _bytes_feature(colorspace),
  File "build_imagenet_data_nobox.py", line 175, in _bytes_feature
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))
TypeError: 'RGB' has type str, but expected one of: bytes
Exception in thread Thread-15:
Traceback (most recent call last):
  File "/home/work/anaconda3/envs/py36_tf/lib/python3.6/threading.py", line 916, in _bootstrap_inner
    self.run()
  File "/home/work/anaconda3/envs/py36_tf/lib/python3.6/threading.py", line 864, in run
    self._target(*self._args, **self._kwargs)
  File "build_imagenet_data_nobox.py", line 395, in _process_image_files_batch
    height, width)
  File "build_imagenet_data_nobox.py", line 213, in _convert_to_example
    'image/colorspace': _bytes_feature(colorspace),
  File "build_imagenet_data_nobox.py", line 175, in _bytes_feature
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))
TypeError: 'RGB' has type str, but expected one of: bytes
Exception in thread Thread-9:
Traceback (most recent call last):
  File "/home/work/anaconda3/envs/py36_tf/lib/python3.6/threading.py", line 916, in _bootstrap_inner
    self.run()
  File "/home/work/anaconda3/envs/py36_tf/lib/python3.6/threading.py", line 864, in run
    self._target(*self._args, **self._kwargs)
  File "build_imagenet_data_nobox.py", line 395, in _process_image_files_batch
    height, width)
  File "build_imagenet_data_nobox.py", line 213, in _convert_to_example
    'image/colorspace': _bytes_feature(colorspace),
  File "build_imagenet_data_nobox.py", line 175, in _bytes_feature
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))
TypeError: 'RGB' has type str, but expected one of: bytes




Exception in thread Thread-1:
Traceback (most recent call last):
  File "/home/work/anaconda3/envs/py36_tf/lib/python3.6/threading.py", line 916, in _bootstrap_inner
    self.run()
  File "/home/work/anaconda3/envs/py36_tf/lib/python3.6/threading.py", line 864, in run
    self._target(*self._args, **self._kwargs)
  File "build_imagenet_data_nobox.py", line 397, in _process_image_files_batch
    height, width)
  File "build_imagenet_data_nobox.py", line 218, in _convert_to_example
    'image/class/synset': _bytes_feature(synset),
  File "build_imagenet_data_nobox.py", line 175, in _bytes_feature
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))
TypeError: 'n03777568' has type str, but expected one of: bytes

```


# 解决方法


```
def _bytes_feature(value):
  """Wrapper for inserting bytes features into Example proto."""
  value = tf.compat.as_bytes(value)
  return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))
```
在_bytes_feature里参加 value=tf.compat.as_bytes(value)