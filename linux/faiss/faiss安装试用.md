

# 1 配置python虚拟环境

```bash
conda create -n py38_faiss python=3.8

conda activate py38_faiss


# 安装pytorch-cpu
pip3 install torch torchvision torchaudio

# CPU-only version
# conda install -c faiss-cpu
pip install faiss-cpu -DFAISS_ENABLE_GPU=OFF -DFAISS_ENABLE_PYTHON=ON -DBUILD_TESTING=ON -DPython_EXECUTABLE=/path/to/python3.7
```

# 2 编译
```bash
cmake -B build .

```

# 3 测试python调用

```bash
cd build/faiss/python
python setup.py build
PYTHONPATH="$(ls -d ./build/faiss/python/build/lib*/)" pytest tests/test_*.py
```

