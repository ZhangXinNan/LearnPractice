

# Environment Setup
```bash
# conda create --name openmmlab python=3.8 -y
# conda activate openmmlab

conda create --name py310_mmocr python=3.10

conda activate py310_mmocr

# pip3 install torch torchvision
pip install torch==1.13.1 torchvision==0.14.1 torchaudio==0.13.1


```

# Installation Steps

## Best Practices
Step 0. Install MMEngine, MMCV and MMDetection using MIM.
```bash
pip install -U openmim
mim install mmengine
mim install mmcv
mim install mmdet
```

### Step 1. Install MMOCR.

### Step 2. (Optional) 


## Verify the installation

```python
from mmocr.apis import MMOCRInferencer
ocr = MMOCRInferencer(det='DBNet', rec='CRNN')
ocr('demo/demo_text_ocr.jpg', show=True, print_result=True)
```