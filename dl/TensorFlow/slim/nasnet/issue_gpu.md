```
INFO:tensorflow:A GPU is available on the machine, consider using NCHW data format for increased speed on GPU.
Traceback (most recent call last):
  File "train_image_classifier.py", line 574, in <module>
    tf.app.run()
  File "/data1/sina_recmd/local/Python-2.7.8/lib/python2.7/site-packages/tensorflow/python/platform/app.py", line 48, in run
    _sys.exit(main(_sys.argv[:1] + flags_passthrough))
  File "train_image_classifier.py", line 474, in main
    clones = model_deploy.create_clones(deploy_config, clone_fn, [batch_queue])
  File "/data1/sina_recmd/home/zhangxin22/github/nasnet-tensorflow/deployment/model_deploy.py", line 193, in create_clones
    outputs = model_fn(*args, **kwargs)
  File "train_image_classifier.py", line 457, in clone_fn
    logits, end_points = network_fn(images)
  File "/data1/sina_recmd/home/zhangxin22/github/nasnet-tensorflow/nets/nets_factory.py", line 135, in network_fn
    return func(images, num_classes, is_training=is_training, **kwargs)
  File "/data1/sina_recmd/home/zhangxin22/github/nasnet-tensorflow/nets/nasnet/nasnet.py", line 370, in build_nasnet_mobile
    final_endpoint=final_endpoint)
  File "/data1/sina_recmd/home/zhangxin22/github/nasnet-tensorflow/nets/nasnet/nasnet.py", line 448, in _build_nasnet_base
    net, cell_outputs = stem()
  File "/data1/sina_recmd/home/zhangxin22/github/nasnet-tensorflow/nets/nasnet/nasnet.py", line 443, in <lambda>
    stem = lambda: _imagenet_stem(images, hparams, stem_cell)
  File "/data1/sina_recmd/home/zhangxin22/github/nasnet-tensorflow/nets/nasnet/nasnet.py", line 264, in _imagenet_stem
    cell_num=cell_num)
  File "/data1/sina_recmd/home/zhangxin22/github/nasnet-tensorflow/nets/nasnet/nasnet_utils.py", line 326, in __call__
    stride, original_input_left)
  File "/data1/sina_recmd/home/zhangxin22/github/nasnet-tensorflow/nets/nasnet/nasnet_utils.py", line 352, in _apply_conv_operation
    net = _stacked_separable_conv(net, stride, operation, filter_size)
  File "/data1/sina_recmd/home/zhangxin22/github/nasnet-tensorflow/nets/nasnet/nasnet_utils.py", line 183, in _stacked_separable_conv
    stride=stride)
  File "/data1/sina_recmd/local/Python-2.7.8/lib/python2.7/site-packages/tensorflow/contrib/framework/python/ops/arg_scope.py", line 181, in func_with_args
    return func(*args, **current_args)
TypeError: separable_convolution2d() got an unexpected keyword argument 'data_format'
```