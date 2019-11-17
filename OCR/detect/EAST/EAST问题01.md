

# 错误
```bash
2257 text boxes before nms
Traceback (most recent call last):
  File "eval.py", line 196, in <module>
    tf.app.run()
  File "/Users/zhangxin/anaconda3/envs/py36_tf/lib/python3.6/site-packages/tensorflow/python/platform/app.py", line 125, in run
    _sys.exit(main(argv))
  File "eval.py", line 162, in main
    boxes, timer = detect(score_map=score, geo_map=geometry, timer=timer)
  File "eval.py", line 100, in detect
    boxes = lanms.merge_quadrangle_n9(boxes.astype('float32'), nms_thres)
  File "/Users/zhangxin/github/EAST/lanms/__init__.py", line 12, in merge_quadrangle_n9
    from .adaptor import merge_quadrangle_n9 as nms_impl
ImportError: dynamic module does not define module export function (PyInit_adaptor)
```

# 


