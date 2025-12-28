
```yaml
Architecture:
  model_type: det
  algorithm: DB
  Transform: null
  Backbone:
    name: PPHGNetV2_B4
    det: True
  Neck:
    name: LKPAN
    out_channels: 256
    intracl: true
  Head:
    name: PFHeadLocal
    k: 50
    mode: "large"
```

```python
# torchocr/modeling/backbones/__init__.py
from .rec_pphgnetv2 import PPHGNetV2_B4
# torchocr/modeling/backbones/rec_pphgnetv2.py

# torchocr/modeling/necks/__init__.py
from .db_fpn import DBFPN, RSEFPN, LKPAN
# torchocr/modeling/necks/db_fpn.py

# torchocr/modeling/heads/__init__.py
from .det_db_head import DBHead, PFHeadLocal
# torchocr/modeling/heads/det_db_head.py
```




