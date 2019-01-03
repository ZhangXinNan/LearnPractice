

# 问题
不使用bounding box

# 解决方法
注释掉一行代码
```
# image_to_bboxes = _build_bounding_box_lookup(FLAGS.bounding_box_file)
image_to_bboxes = {}
```