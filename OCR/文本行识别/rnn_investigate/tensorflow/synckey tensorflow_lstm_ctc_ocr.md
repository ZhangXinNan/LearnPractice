
[synckey/tensorflow_lstm_ctc_ocr](https://github.com/synckey/tensorflow_lstm_ctc_ocr)

## train
### mac
```
Traceback (most recent call last):
  File "lstm_and_ctc_ocr_train.py", line 132, in <module>
    train()
  File "lstm_and_ctc_ocr_train.py", line 112, in train
    c, steps = do_batch()
  File "lstm_and_ctc_ocr_train.py", line 90, in do_batch
    do_report()
  File "lstm_and_ctc_ocr_train.py", line 83, in do_report
    report_accuracy(dd, test_targets)
  File "lstm_and_ctc_ocr_train.py", line 35, in report_accuracy
    original_list = decode_sparse_tensor(test_targets)
  File "/Users/zhangxin/github/tensorflow_lstm_ctc_ocr/utils.py", line 128, in decode_sparse_tensor
    result.append(decode_a_seq(index, sparse_tensor))
  File "/Users/zhangxin/github/tensorflow_lstm_ctc_ocr/utils.py", line 101, in decode_a_seq
    str = common.DIGITS[spars_tensor[1][m]]
IndexError: string index out of range

```

### 142
```
Traceback (most recent call last):
  File "lstm_and_ctc_ocr_train.py", line 132, in <module>
    train()
  File "lstm_and_ctc_ocr_train.py", line 62, in train
    loss = tf.nn.ctc_loss( targets, logits, seq_len)
  File "/usr/lib/python2.7/site-packages/tensorflow/python/ops/ctc_ops.py", line 132, in ctc_loss
    raise TypeError("Expected labels to be a SparseTensor")
TypeError: Expected labels to be a SparseTensor
```

