
错误1
```
2018-02-07 16:59:00,091 INFO Starting inference using data/demo/demo.png as input
Traceback (most recent call last):
  File "demo.py", line 228, in <module>
    tf.app.run()
  File "/Users/zhangxin/anaconda2/envs/tensorflow/lib/python2.7/site-packages/tensorflow/python/platform/app.py", line 48, in run
    _sys.exit(main(_sys.argv[:1] + flags_passthrough))
  File "demo.py", line 165, in main
    image = scp.misc.imread(input_image)
AttributeError: 'module' object has no attribute 'imread'
```

解决方法：
```
conda install PILLOW
```