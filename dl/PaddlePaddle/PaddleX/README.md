

# 安装
```bash
conda create -n paddlex python=3.9

conda activate paddlex

# 安装 PaddlePaddle
# cpu
python -m pip install paddlepaddle==3.0.0rc0 -i https://www.paddlepaddle.org.cn/packages/stable/cpu/

# gpu，该命令仅适用于 CUDA 版本为 11.8 的机器环境
python -m pip install paddlepaddle-gpu==3.0.0rc0 -i https://www.paddlepaddle.org.cn/packages/stable/cu118/

# gpu，该命令仅适用于 CUDA 版本为 12.3 的机器环境
python -m pip install paddlepaddle-gpu==3.0.0rc0 -i https://www.paddlepaddle.org.cn/packages/stable/cu123/

# 测试
python -c "import paddle; print(paddle.__version__)"


# 安装PaddleX
## wheel包安装：模型推理与集成
pip install https://paddle-model-ecology.bj.bcebos.com/paddlex/whl/paddlex-3.0.0rc0-py3-none-any.whl

## 插件安装模式：二次开发
git clone https://github.com/PaddlePaddle/PaddleX.git
cd PaddleX
pip install -e .
# paddlex --install PaddleXXX  # 例如PaddleOCR
paddlex --install PaddleOCR PaddleClas
```

# 使用
```bash
paddlex --pipeline OCR --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_ocr_002.png --device gpu:0

paddlex --pipeline OCR --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_ocr_002.png --device cpu


paddlex --pipeline doc_preprocessor --input doc_test_rotated.jpg --use_doc_orientation_classify True --use_doc_unwarping True --save_path ./output --device cpu

paddlex --pipeline OCR --input https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/general_ocr_002.png --use_doc_orientation_classify False --use_doc_unwarping False --use_textline_orientation False --save_path ./output --device gpu:0

```