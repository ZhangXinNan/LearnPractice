
# 安装
```bash
pip install fastapi
pip install uvicorn
```

# 代码及说明
```python
# 导入 FastAPI
from fastapi import FastAPI

# 创建一个 FastAPI「实例」
# 这个实例将是创建你所有 API 的主要交互对象。
app = FastAPI()

# 这里的「路径」指的是 URL 中从第一个 / 起的后半部分。
# 定义一个路径操作装饰器
'''
@app.get("/") 告诉 FastAPI 在它下方的函数负责处理如下访问请求：
    请求路径为 /
    使用 get 操作
'''
@app.get("/")
# 定义路径操作函数
async def root():
    return {"message": "Hello World"}
```

# 运行
```bash
uvicorn main:app --reload
```

