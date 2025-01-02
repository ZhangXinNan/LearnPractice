
```bash
conda create -n py39_pytorch_ocr python=3.9

conda activate py39_pytorch_ocr
conda deactivate

pip install -r requirements.txt

# paddlepaddle
python -m pip install paddlepaddle==2.6.1 -i https://pypi.tuna.tsinghua.edu.cn/simple

# pytorch
pip3 install torch torchvision torchaudio


```