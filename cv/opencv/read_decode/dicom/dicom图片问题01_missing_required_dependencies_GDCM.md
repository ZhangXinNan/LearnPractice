

# 1 问题
```bash
(py36_urs) ➜  src git:(zxdev_allinone) ✗ python image_reader_dicom.py
Traceback (most recent call last):
  File "image_reader_dicom.py", line 81, in <module>
    main()
  File "image_reader_dicom.py", line 70, in main
    print(type(ds.pixel_array), ds.pixel_array.shape)
  File "/Users/zhangxin/opt/anaconda3/envs/py36_urs/lib/python3.6/site-packages/pydicom/dataset.py", line 1615, in pixel_array
    self.convert_pixel_data()
  File "/Users/zhangxin/opt/anaconda3/envs/py36_urs/lib/python3.6/site-packages/pydicom/dataset.py", line 1324, in convert_pixel_data
    self._convert_pixel_data_without_handler()
  File "/Users/zhangxin/opt/anaconda3/envs/py36_urs/lib/python3.6/site-packages/pydicom/dataset.py", line 1409, in _convert_pixel_data_without_handler
    raise RuntimeError(msg + ', '.join(pkg_msg))
RuntimeError: The following handlers are available to decode the pixel data however they are missing required dependencies: GDCM (req. GDCM)
```

# 2 解决方法


