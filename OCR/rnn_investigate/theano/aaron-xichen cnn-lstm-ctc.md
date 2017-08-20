
## mac
### 'module' object has no attribute 'find_graphviz'
```
➜  cnn-lstm-ctc git:(zxdev) ✗ sh train.sh 
Traceback (most recent call last):
  File "train/train.py", line 7, in <module>
    import theano
  File "/usr/local/lib/python2.7/site-packages/theano/__init__.py", line 74, in <module>
    from theano.printing import pprint, pp
  File "/usr/local/lib/python2.7/site-packages/theano/printing.py", line 35, in <module>
    if pd.find_graphviz():
AttributeError: 'module' object has no attribute 'find_graphviz'
```

```
pip uninstall pydot
```


### train
```
➜  cnn-lstm-ctc git:(zxdev) ✗ ./train.sh                                                           
/usr/local/lib/python2.7/site-packages/theano/tensor/signal/downsample.py:6: UserWarning: downsample module has been moved to the theano.tensor.signal.pool module.
  "downsample module has been moved to the theano.tensor.signal.pool module.")
loaded 29143 samples from ./dataset/english_sentence/train_img_list.txt
loaded 2914 samples from ./dataset/english_sentence/val_img_list.txt
building symbolic tensors(0.168231964111)
setting parameters(0.172531843185)
('n_classes: ', 95)
('multi-step: ', set([79625, 68250, 45500]))
building the model(0.173081874847)
computing updates and function(1.16841292381)
using normal sgd and learning_rate:0.00999999977648
('bw_lstm_b', <class 'theano.tensor.sharedvar.TensorSharedVariable'>)
('fw_lstm_W', <class 'theano.tensor.sharedvar.TensorSharedVariable'>)
('fw_lstm_U', <class 'theano.tensor.sharedvar.TensorSharedVariable'>)
('fw_lstm_b', <class 'theano.tensor.sharedvar.TensorSharedVariable'>)
('bw_lstm_W', <class 'theano.tensor.sharedvar.TensorSharedVariable'>)
('bw_lstm_U', <class 'theano.tensor.sharedvar.TensorSharedVariable'>)
('hidden_b', <class 'theano.tensor.sharedvar.TensorSharedVariable'>)
('hidden_W', <class 'theano.tensor.sharedvar.TensorSharedVariable'>)
building training function(3.80952906609)
building validating function(216.033226967)
begin to train(236.545507908)
.epoch 1/200 begin(236.546)
[prefetch]height: 28, x_max_step:132.0, y_max_width:50
Traceback (most recent call last):
  File "train/train.py", line 139, in <module>
    x_slice, x_mask_slice, y_slice, y_clip_slice = training_data_prefetcher.fetch_next(True)
  File "/Users/zhangxin/github/cnn-lstm-ctc/layers/utee.py", line 122, in fetch_next
    values = self._wrap(features, labels, self.batch_size, self.stride, self.patch_width, self.n_classes, self.is_shared, is_blank_y)
  File "/Users/zhangxin/github/cnn-lstm-ctc/layers/utee.py", line 137, in _wrap
    x = np.zeros((batch_size, 1, height, x_max_len)). astype(config.floatX)
TypeError: 'numpy.float64' object cannot be interpreted as an index
```