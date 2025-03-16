

https://github.com/open-mmlab/mmpose


# 安装
https://mmpose.readthedocs.io/en/latest/installation.html

The main branch works with PyTorch 1.8+.

Step 0. Download and install Miniconda from the official website.

Step 1. Create a conda environment and activate it.
```bash
conda create --name openmmlab python=3.8 -y
conda activate openmmlab
```

Step 2. Install PyTorch following official instructions, e.g.

```bash
# On GPU platforms:
# conda install pytorch torchvision -c pytorch
# cuda 11.2
pip install torch==1.10.1+cu111 torchvision==0.11.2+cu111 torchaudio==0.10.1 -f https://download.pytorch.org/whl/cu111/torch_stable.html
# On CPU platforms:
conda install pytorch torchvision cpuonly -c pytorch
```

Step 3. Install MMEngine and MMCV using MIM.
```bash
pip install -U openmim
mim install mmengine
mim install "mmcv>=2.0.1"
pip install mmcv==2.0.1

# Note that some of the demo scripts in MMPose require MMDetection (mmdet) for human detection. 
# If you want to run these demo scripts with mmdet, you can easily install mmdet as a dependency by running:
mim install "mmdet>=3.1.0"
```

