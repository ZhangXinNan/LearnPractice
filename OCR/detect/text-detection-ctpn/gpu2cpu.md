 (1) Set "USE_GPU_NMS " in the file ./ctpn/text.yml as "False"
 (2) Set the "__C.USE_GPU_NMS" in the file ./lib/fast_rcnn/config.py as "False";
 (3) Comment out the line ```from lib.utils.gpu_nms import gpu_nms``` in the file ./lib/fast_rcnn/nms_wrapper.py;
 Comment out the line ```from . import gpu_nms``` in the file lib/utils/__init__.py.
 (4) To modify and rebuild the setup.py.
Modify setup.py: 
```
from Cython.Build import cythonize
import numpy as np
from distutils.core import setup
from distutils.extension import Extension

try:
    numpy_include = np.get_include()
except AttributeError:
    numpy_include = np.get_numpy_include()

ext_modules = [
    Extension(
        'bbox',
        sources=['bbox.c'],
        include_dirs = [numpy_include]
    ),
    Extension(
        'cython_nms',
        sources=['cython_nms.c'],
        include_dirs = [numpy_include]
    )
]
setup(
    ext_modules=ext_modules
)
```

rebuild:
```
export CFLAGS=~/anaconda2/lib/python2.7/site-packages/numpy/core/include
python setup.py build
```


(5) then copy .so to xxx/text-detection-ctpn-master/lib/utils
```
cd text-detection-ctpn-master
python demo.py
```

