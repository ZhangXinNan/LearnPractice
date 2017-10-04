
问题
```
Loaded network /data/zhangxin/github/py-faster-rcnn/data/faster_rcnn_models/VGG16_faster_rcnn_final.caffemodel
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Demo for data/demo/000456.jpg
Detection took 0.258s for 300 object proposals
Traceback (most recent call last):
  File "./tools/demo.py", line 149, in <module>
    demo(net, im_name)
  File "./tools/demo.py", line 98, in demo
    vis_detections(im, cls, dets, thresh=CONF_THRESH)
  File "./tools/demo.py", line 47, in vis_detections
    fig, ax = plt.subplots(figsize=(12, 12))
  File "/data/anaconda2/lib/python2.7/site-packages/matplotlib/pyplot.py", line 1202, in subplots
    fig = figure(**fig_kw)
  File "/data/anaconda2/lib/python2.7/site-packages/matplotlib/pyplot.py", line 535, in figure
    **kwargs)
  File "/data/anaconda2/lib/python2.7/site-packages/matplotlib/backends/backend_qt5agg.py", line 44, in new_figure_manager
    return new_figure_manager_given_figure(num, thisFig)
  File "/data/anaconda2/lib/python2.7/site-packages/matplotlib/backends/backend_qt5agg.py", line 51, in new_figure_manager_given_figure
    canvas = FigureCanvasQTAgg(figure)
  File "/data/anaconda2/lib/python2.7/site-packages/matplotlib/backends/backend_qt5agg.py", line 242, in __init__
    super(FigureCanvasQTAgg, self).__init__(figure=figure)
  File "/data/anaconda2/lib/python2.7/site-packages/matplotlib/backends/backend_qt5agg.py", line 66, in __init__
    super(FigureCanvasQTAggBase, self).__init__(figure=figure)
  File "/data/anaconda2/lib/python2.7/site-packages/matplotlib/backends/backend_qt5.py", line 236, in __init__
    _create_qApp()
  File "/data/anaconda2/lib/python2.7/site-packages/matplotlib/backends/backend_qt5.py", line 144, in _create_qApp
    raise RuntimeError('Invalid DISPLAY variable')
RuntimeError: Invalid DISPLAY variable
OpenCV Error: Assertion failed (key_ == -1) in ~TLSDataContainer, file /data/cv/Software/opencv-3.2.0/modules/core/src/system.cpp, line 1186
terminate called after throwing an instance of 'cv::Exception'
  what():  /data/cv/Software/opencv-3.2.0/modules/core/src/system.cpp:1186: error: (-215) key_ == -1 in function ~TLSDataContainer
```