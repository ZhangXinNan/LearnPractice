

# python 
```bash
# 使用虚拟环境
conda activate py36_grpc

# First, install the grpcio-tools package:
pip install grpcio-tools

# generate the Python code:
python -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/route_guide.proto

# Run the server, which will listen on port 50051:
python route_guide_server.py

# Run the client (in a different terminal):
python route_guide_client.py
```


# c++
## mac

```bash
brew install autoconf automake libtool shtool

brew install gflags

LIBTOOL=glibtool LIBTOOLIZE=glibtoolize make

```

