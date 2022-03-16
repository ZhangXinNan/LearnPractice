# 问题

```bash
Traceback (most recent call last):
  File "auto_service.py", line 257, in auto_recog_multi
    box_list, score_list = det_yolo.detect_car_multi(img)
  File "/home/app/gitlab/auto_service/src/detector_yolo5_v6.py", line 71, in detect_car_multi
    pred = self.model(img, augment=self.augment)
  File "/home/app/miniconda3/envs/py37_auto_service/lib/python3.7/site-packages/torch/nn/modules/module.py", line 727, in _call_impl
    result = self.forward(*input, **kwargs)
  File "/home/app/github/yolov5/models/common.py", line 384, in forward
    y = self.model(im) if self.jit else self.model(im, augment=augment, visualize=visualize)
  File "/home/app/miniconda3/envs/py37_auto_service/lib/python3.7/site-packages/torch/nn/modules/module.py", line 727, in _call_impl
    result = self.forward(*input, **kwargs)
  File "/home/app/github/yolov5/models/yolo.py", line 126, in forward
    return self._forward_once(x, profile, visualize)  # single-scale inference, train
  File "/home/app/github/yolov5/models/yolo.py", line 149, in _forward_once
    x = m(x)  # run
  File "/home/app/miniconda3/envs/py37_auto_service/lib/python3.7/site-packages/torch/nn/modules/module.py", line 727, in _call_impl
    result = self.forward(*input, **kwargs)
  File "/home/app/github/yolov5/models/yolo.py", line 62, in forward
    y[..., 0:2] = (y[..., 0:2] * 2 - 0.5 + self.grid[i]) * self.stride[i]  # xy
RuntimeError: The size of tensor a (24) must match the size of tensor b (32) at non-singleton dimension 3
```

# 解决办法






