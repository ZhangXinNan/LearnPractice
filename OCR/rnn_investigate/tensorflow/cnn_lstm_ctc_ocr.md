[weinman/cnn_lstm_ctc_ocr](https://github.com/weinman/cnn_lstm_ctc_ocr)


# 问题1
```
Caused by op u'train/CTCLoss', defined at:
  File "train_6880.py", line 210, in <module>
    tf.app.run()
  File "/usr/local/lib/python2.7/site-packages/tensorflow/python/platform/app.py", line 48, in run
    _sys.exit(main(_sys.argv[:1] + flags_passthrough))
  File "train_6880.py", line 180, in main
    train_op = _get_training(logits,label,sequence_length)
  File "train_6880.py", line 113, in _get_training
    loss = model.ctc_loss_layer(rnn_logits,label,sequence_length)
  File "/Users/zhangxin/github/cnn_lstm_ctc_ocr/src/model.py", line 167, in ctc_loss_layer
    time_major=True )
  File "/usr/local/lib/python2.7/site-packages/tensorflow/python/ops/ctc_ops.py", line 152, in ctc_loss
    ignore_longer_outputs_than_inputs=ignore_longer_outputs_than_inputs)
  File "/usr/local/lib/python2.7/site-packages/tensorflow/python/ops/gen_ctc_ops.py", line 223, in _ctc_loss
    name=name)
  File "/usr/local/lib/python2.7/site-packages/tensorflow/python/framework/op_def_library.py", line 787, in _apply_op_helper
    op_def=op_def)
  File "/usr/local/lib/python2.7/site-packages/tensorflow/python/framework/ops.py", line 2956, in create_op
    op_def=op_def)
  File "/usr/local/lib/python2.7/site-packages/tensorflow/python/framework/ops.py", line 1470, in __init__
    self._traceback = self._graph._extract_stack()  # pylint: disable=protected-access

InvalidArgumentError (see above for traceback): Saw a non-null label (index >= num_classes - 1) following a null label, batch: 6 num_classes: 6881 labels: 6216,2200
	 [[Node: train/CTCLoss = CTCLoss[ctc_merge_repeated=true, ignore_longer_outputs_than_inputs=false, preprocess_collapse_repeated=false, _device="/job:localhost/replica:0/task:0/device:CPU:0"](rnn/logits/Relu, DeserializeManySparse, Cast_1, convnet/seq_len)]]
```