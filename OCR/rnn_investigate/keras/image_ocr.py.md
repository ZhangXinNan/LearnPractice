[keras image_ocr.py](https://github.com/fchollet/keras/blob/master/examples/image_ocr.py)


### mac
#### 问题1
```
(tf) ➜  examples git:(zxdev) ✗ python image_ocr.py   
Traceback (most recent call last):
  File "image_ocr.py", line 42, in <module>
    import pylab
  File "/Users/zhangxin/github/Attention-OCR/tf/lib/python2.7/site-packages/pylab.py", line 1, in <module>
    from matplotlib.pylab import *
  File "/Users/zhangxin/github/Attention-OCR/tf/lib/python2.7/site-packages/matplotlib/pylab.py", line 257, in <module>
    from matplotlib import cbook, mlab, pyplot as plt
  File "/Users/zhangxin/github/Attention-OCR/tf/lib/python2.7/site-packages/matplotlib/pyplot.py", line 115, in <module>
    _backend_mod, new_figure_manager, draw_if_interactive, _show = pylab_setup()
  File "/Users/zhangxin/github/Attention-OCR/tf/lib/python2.7/site-packages/matplotlib/backends/__init__.py", line 32, in pylab_setup
    globals(),locals(),[backend_name],0)
  File "/Users/zhangxin/github/Attention-OCR/tf/lib/python2.7/site-packages/matplotlib/backends/backend_macosx.py", line 19, in <module>
    from matplotlib.backends import _macosx
RuntimeError: Python is not installed as a framework. The Mac OS X backend will not be able to function correctly if Python is not installed as a framework. See the Python documentation for more information on installing Python as a framework on Mac OS X. Please either reinstall Python as a framework, or try one of the other backends. If you are using (Ana)Conda please install python.app and replace the use of 'python' with 'pythonw'. See 'Working with Matplotlib on OSX' in the Matplotlib FAQ for more information.
```
解决方法：
```
Problem Cause In mac os image rendering back end of matplotlib (what-is-a-backend to render using the API of Cocoa by default). There is Qt4Agg and GTKAgg and as a back-end is not the default. Set the back end of macosx that is differ compare with other windows or linux os.

I resolve this issue following ways:

I assume you have installed the pip matplotlib, there is a directory in you root called ~/.matplotlib.
Create a file ~/.matplotlib/matplotlibrc there and add the following code: backend: TkAgg
From this link you can try different diagram.
```

#### 问题2
```
ImportError: `save_weights` requires h5py.
```

解决方法：
```
pip install h5py
```


### seele
```
distutils.errors.DistutilsError: Setup script exited with error: command 'x86_64-linux-gnu-gcc' failed with exit status 1

----------------------------------------
Cleaning up...
Command python setup.py egg_info failed with error code 1 in /home/zhangxin/tensorflow/build/cairocffi
Traceback (most recent call last):
  File "/home/zhangxin/tensorflow/bin/pip", line 11, in <module>
    sys.exit(main())
  File "/home/zhangxin/tensorflow/local/lib/python2.7/site-packages/pip/__init__.py", line 185, in main
    return command.main(cmd_args)
  File "/home/zhangxin/tensorflow/local/lib/python2.7/site-packages/pip/basecommand.py", line 161, in main
    text = '\n'.join(complete_log)
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe6 in position 49: ordinal not in range(128)
```


### 142
#### 问题1 no module cairocffi
```
[zhangxin0627@l22-240-142 examples]$ pip install cairocffi
Requirement already satisfied: cairocffi in /usr/local/lib/python3.4/site-packages
Requirement already satisfied: cffi>=1.1.0 in /usr/local/lib/python3.4/site-packages (from cairocffi)
Requirement already satisfied: pycparser in /usr/local/lib/python3.4/site-packages (from cffi>=1.1.0->cairocffi)
[zhangxin0627@l22-240-142 examples]$ python image_ocr.py  
Traceback (most recent call last):
  File "image_ocr.py", line 38, in <module>
    import cairocffi as cairo
ImportError: No module named cairocffi
You have mail in /var/spool/mail/root
```
解决方案：
```
 pip2 install cairocffi
 pip2 install editdistance
```

#### 问题2 No module named merge
```
[root@l22-240-142 examples]# python2 image_ocr.py
Using TensorFlow backend.
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcublas.so locally
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcudnn.so locally
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcufft.so locally
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcuda.so.1 locally
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcurand.so locally
Traceback (most recent call last):
  File "image_ocr.py", line 50, in <module>
    from keras.layers.merge import add, concatenate
ImportError: No module named merge
```

#### 问题3 h5py
```
12799/12800 [============================>.] - ETA: 0s - loss: 0.5847Traceback (most recent call last):
  File "image_ocr.py", line 492, in <module>
    train(run_name, 0, 20, 128)
  File "image_ocr.py", line 487, in train
    callbacks=[viz_cb, img_gen], initial_epoch=start_epoch)
  File "/data/zhangxin/github/keras/examples/venv2/lib/python2.7/site-packages/keras/legacy/interfaces.py", line 88, in wrapper
    return func(*args, **kwargs)
  File "/data/zhangxin/github/keras/examples/venv2/lib/python2.7/site-packages/keras/engine/training.py", line 1927, in fit_generator
    callbacks.on_epoch_end(epoch, epoch_logs)
  File "/data/zhangxin/github/keras/examples/venv2/lib/python2.7/site-packages/keras/callbacks.py", line 77, in on_epoch_end
    callback.on_epoch_end(epoch, logs)
  File "image_ocr.py", line 380, in on_epoch_end
    self.model.save_weights(os.path.join(self.output_dir, 'weights%02d.h5' % (epoch)))
  File "/data/zhangxin/github/keras/examples/venv2/lib/python2.7/site-packages/keras/engine/topology.py", line 2496, in save_weights
    raise ImportError('`save_weights` requires h5py.')
ImportError: `save_weights` requires h5py.
```
解决方法：
```
pip install h5py
```

### docker caffe 
```
ImportError: No module named extern
```


### docker tensorflow


安装cairocffi，解决方法:
["No package 'libffi' found" error during pip install](https://github.com/Kozea/cairocffi/issues/14), 
[Install tkinter for Python](https://stackoverflow.com/questions/4783810/install-tkinter-for-python)
```
apt-get install python-cffi
apt-get install python-tk
```

安装 h5py
```
apt-get install h5py
```



