

# 1 问题

```bash
2021-02-12 02:17:46 [INFO]      Start evaluating (total_samples=100, total_iters=100)...
Traceback (most recent call last):
  File "train.py", line 141, in <module>
    main(args)
  File "train.py", line 136, in main
    losses=losses)
  File "/Users/zhangxin/github/PaddleSeg/paddleseg/core/train.py", line 179, in train
    model, val_dataset, num_workers=num_workers)
  File "/Users/zhangxin/github/PaddleSeg/paddleseg/core/val.py", line 110, in evaluate
    crop_size=crop_size)
  File "/Users/zhangxin/github/PaddleSeg/paddleseg/core/infer.py", line 179, in inference
    pred = reverse_transform(pred, ori_shape, transforms)
  File "/Users/zhangxin/github/PaddleSeg/paddleseg/core/infer.py", line 54, in reverse_transform
    pred = F.interpolate(pred, (h, w), mode='nearest')
  File "/opt/anaconda3/envs/py37_paddle2/lib/python3.7/site-packages/paddle/nn/functional/common.py", line 485, in interpolate
    out = core.ops.nearest_interp_v2(x, *dy_attr)
RuntimeError: (NotFound) Operator nearest_interp_v2 does not have kernel for data_type[int]:data_layout[ANY_LAYOUT]:place[CPUPlace]:library_type[PLAIN].
  [Hint: Expected kernel_iter != kernels.end(), but received kernel_iter == kernels.end().] (at /home/teamcity/work/ef54dc8a5b211854/paddle/fluid/imperative/prepared_operator.cc:118)
  [Hint: If you need C++ stacktraces for debugging, please set `FLAGS_call_stack_level=2`.]
  [operator < nearest_interp_v2 > error]
```
