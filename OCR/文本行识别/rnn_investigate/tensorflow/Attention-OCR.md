## install
```
pip install pillow
pip install tqdm
```



## train
```
python src/launcher.py --phase=train --data-path=sample/sample.txt --data-base-dir=sample --log-path=log.txt --no-load-model
```


### mac 上问题
```
Traceback (most recent call last):
  File "src/launcher.py", line 146, in <module>
    main(sys.argv[1:], exp_config.ExpConfig)
  File "src/launcher.py", line 142, in main
    session = sess)
  File "/Users/zhangxin/github/Attention-OCR/src/model/model.py", line 151, in __init__
    use_gru = use_gru)
  File "/Users/zhangxin/github/Attention-OCR/src/model/seq2seq_model.py", line 141, in __init__
    softmax_loss_function=softmax_loss_function)
  File "/Users/zhangxin/github/Attention-OCR/src/model/seq2seq.py", line 993, in model_with_buckets
    decoder_inputs[:int(bucket[1])], int(bucket[0]))
  File "/Users/zhangxin/github/Attention-OCR/src/model/seq2seq_model.py", line 140, in <lambda>
    self.target_weights, buckets, lambda x, y, z: seq2seq_f(x, y, z, False),
  File "/Users/zhangxin/github/Attention-OCR/src/model/seq2seq_model.py", line 122, in seq2seq_f
    attn_num_hidden = attn_num_hidden)
  File "/Users/zhangxin/github/Attention-OCR/src/model/seq2seq.py", line 675, in embedding_attention_decoder
    initial_state_attention=initial_state_attention, attn_num_hidden=attn_num_hidden)
  File "/Users/zhangxin/github/Attention-OCR/src/model/seq2seq.py", line 577, in attention_decoder
    cell_output, state = cell(x, state)
  File "/Users/zhangxin/github/Attention-OCR/tf/lib/python2.7/site-packages/tensorflow/contrib/rnn/python/ops/core_rnn_cell_impl.py", line 953, in __call__
    cur_inp, new_state = cell(cur_inp, cur_state)
  File "/Users/zhangxin/github/Attention-OCR/tf/lib/python2.7/site-packages/tensorflow/contrib/rnn/python/ops/core_rnn_cell_impl.py", line 235, in __call__
    with _checked_scope(self, scope or "basic_lstm_cell", reuse=self._reuse):
  File "/usr/local/Cellar/python/2.7.13/Frameworks/Python.framework/Versions/2.7/lib/python2.7/contextlib.py", line 17, in __enter__
    return self.gen.next()
  File "/Users/zhangxin/github/Attention-OCR/tf/lib/python2.7/site-packages/tensorflow/contrib/rnn/python/ops/core_rnn_cell_impl.py", line 77, in _checked_scope
    type(cell).__name__))
ValueError: Attempt to reuse RNNCell <tensorflow.contrib.rnn.python.ops.core_rnn_cell_impl.BasicLSTMCell object at 0x1143ebfd0> with a different variable scope than its first use.  First use of cell was with scope 'embedding_attention_decoder/attention_decoder/multi_rnn_cell/cell_0/basic_lstm_cell', this attempt is with scope 'embedding_attention_decoder/attention_decoder/multi_rnn_cell/cell_1/basic_lstm_cell'.  Please create a new instance of the cell if you would like it to use a different set of weights.  If before you were using: MultiRNNCell([BasicLSTMCell(...)] * num_layers), change to: MultiRNNCell([BasicLSTMCell(...) for _ in range(num_layers)]).  If before you were using the same cell instance as both the forward and reverse cell of a bidirectional RNN, simply create two instances (one for forward, one for reverse).  In May 2017, we will start transitioning this cell's behavior to use existing stored weights, if any, when it is called with scope=None (which can lead to silent model degradation, so this error will remain until then.)

```


### 142上问题
```
[zhangxin0627@l22-240-142 Attention-OCR]$ python src/launcher.py --phase=train --data-path=sample/sample.txt --data-base-dir=sample --log-path=log.txt --no-load-model
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcublas.so locally
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcudnn.so locally
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcufft.so locally
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcuda.so.1 locally
I tensorflow/stream_executor/dso_loader.cc:111] successfully opened CUDA library libcurand.so locally
Traceback (most recent call last):
  File "src/launcher.py", line 11, in <module>
    from model.model import Model
  File "/data/zhangxin/github/Attention-OCR/src/model/model.py", line 17, in <module>
    from .seq2seq_model import Seq2SeqModel
  File "/data/zhangxin/github/Attention-OCR/src/model/seq2seq_model.py", line 33, in <module>
    from .seq2seq import model_with_buckets
  File "/data/zhangxin/github/Attention-OCR/src/model/seq2seq.py", line 71, in <module>
    from tensorflow.contrib.rnn.python.ops import rnn, rnn_cell
ImportError: cannot import name rnn
```


### seele
```
(tensorflow)zhangxin@seele:~/github/Attention-OCR$ python src/launcher.py --phase=train --data-path=sample/sample.txt --data-base-dir=sample --log-path=log.txt --no-load-model
I tensorflow/stream_executor/dso_loader.cc:128] successfully opened CUDA library libcublas.so locally
I tensorflow/stream_executor/dso_loader.cc:128] successfully opened CUDA library libcudnn.so locally
I tensorflow/stream_executor/dso_loader.cc:128] successfully opened CUDA library libcufft.so locally
I tensorflow/stream_executor/dso_loader.cc:128] successfully opened CUDA library libcuda.so.1 locally
I tensorflow/stream_executor/dso_loader.cc:128] successfully opened CUDA library libcurand.so locally
I tensorflow/stream_executor/cuda/cuda_gpu_executor.cc:937] successful NUMA node read from SysFS had negative value (-1), but there must be at least one NUMA node, so returning NUMA node zero
I tensorflow/core/common_runtime/gpu/gpu_device.cc:885] Found device 0 with properties: 
name: GeForce GTX 1070
major: 6 minor: 1 memoryClockRate (GHz) 1.7845
pciBusID 0000:01:00.0
Total memory: 7.92GiB
Free memory: 7.45GiB
I tensorflow/core/common_runtime/gpu/gpu_device.cc:906] DMA: 0 
I tensorflow/core/common_runtime/gpu/gpu_device.cc:916] 0:   Y 
I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: GeForce GTX 1070, pci bus id: 0000:01:00.0)
2017-05-18 13:42:56,649 root  INFO     loading data
2017-05-18 13:42:56,650 root  INFO     phase: train
2017-05-18 13:42:56,650 root  INFO     model_dir: train
2017-05-18 13:42:56,650 root  INFO     load_model: False
2017-05-18 13:42:56,650 root  INFO     output_dir: results
2017-05-18 13:42:56,650 root  INFO     steps_per_checkpoint: 500
2017-05-18 13:42:56,650 root  INFO     batch_size: 64
2017-05-18 13:42:56,650 root  INFO     num_epoch: 1000
2017-05-18 13:42:56,650 root  INFO     learning_rate: 1
2017-05-18 13:42:56,650 root  INFO     reg_val: 0
2017-05-18 13:42:56,650 root  INFO     max_gradient_norm: 5.000000
2017-05-18 13:42:56,650 root  INFO     clip_gradients: True
2017-05-18 13:42:56,650 root  INFO     valid_target_length inf
2017-05-18 13:42:56,650 root  INFO     target_vocab_size: 39
2017-05-18 13:42:56,650 root  INFO     target_embedding_size: 10.000000
2017-05-18 13:42:56,650 root  INFO     attn_num_hidden: 128
2017-05-18 13:42:56,650 root  INFO     attn_num_layers: 2
2017-05-18 13:42:56,650 root  INFO     visualize: True
2017-05-18 13:42:56,650 root  INFO     buckets
2017-05-18 13:42:56,650 root  INFO     [(16, 11), (27, 17), (35, 19), (64, 22), (80, 32)]
input_tensor dim: (?, 1, 32, ?)
CNN outdim before squeeze: (?, 1, ?, 512)
CNN outdim: (?, ?, 512)
Traceback (most recent call last):
  File "src/launcher.py", line 146, in <module>
    main(sys.argv[1:], exp_config.ExpConfig)
  File "src/launcher.py", line 142, in main
    session = sess)
  File "/home/zhangxin/github/Attention-OCR/src/model/model.py", line 135, in __init__
    self.concat_conv_output = tf.concat(axis=1, values=[self.conv_output, self.zero_paddings])
TypeError: concat() got an unexpected keyword argument 'axis'
```