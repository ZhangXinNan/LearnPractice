

# 问题
```
Exception in thread Thread-12:
Traceback (most recent call last):
  File "/home/work/anaconda3/envs/py36_tf/lib/python3.6/threading.py", line 916, in _bootstrap_inner
    self.run()
  File "/home/work/anaconda3/envs/py36_tf/lib/python3.6/threading.py", line 864, in run
    self._target(*self._args, **self._kwargs)
  File "build_imagenet_data_nobox.py", line 389, in _process_image_files_batch
    image_buffer, height, width = _process_image(filename, coder)
  File "build_imagenet_data_nobox.py", line 317, in _process_image
    image_data = tf.gfile.FastGFile(filename, 'r').read()
  File "/home/work/anaconda3/envs/py36_tf/lib/python3.6/site-packages/tensorflow/python/lib/io/file_io.py", line 132, in read
    pywrap_tensorflow.ReadFromStream(self._read_buf, length, status))
  File "/home/work/anaconda3/envs/py36_tf/lib/python3.6/site-packages/tensorflow/python/lib/io/file_io.py", line 100, in _prepare_value
    return compat.as_str_any(val)
  File "/home/work/anaconda3/envs/py36_tf/lib/python3.6/site-packages/tensorflow/python/util/compat.py", line 107, in as_str_any
    return as_str(value)
  File "/home/work/anaconda3/envs/py36_tf/lib/python3.6/site-packages/tensorflow/python/util/compat.py", line 80, in as_text
    return bytes_or_text.decode(encoding)
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte

```


# 解决方法
```
# build_imagenet_data.py
# image_data = tf.gfile.FastGFile(filename, 'r').read()
image_data = tf.gfile.FastGFile(filename, 'rb').read()
```