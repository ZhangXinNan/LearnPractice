# 安装依赖
编译和使用TensorFlow Serving， 需要先解决一些先决条件。
## Bazel
## gRPC

# 从源码安装 
## Clone the TensorFlow Serving repository
```
git clone --recurse-submodules https://github.com/tensorflow/serving
cd serving
```

## Install prerequisites
```
cd tensorflow
./configure
cd ..
```

## Build
To build the entire tree, execute:
```
bazel build tensorflow_serving/...
```
Binaries are placed in the bazel-bin directory, and can be run using a command like:
```
bazel-bin/tensorflow_serving/model_servers/tensorflow_model_server
```
To test your installation, execute:
```
bazel test tensorflow_serving/...
```

## Continuous integration build
我们使用TensorFlow ci_build基础设施的持续集成构建为您提供了使用docker的简化开发。 所有你需要的是git和docker。 无需手动安装所有其他依赖项。
```
git clone --recursive https://github.com/tensorflow/serving
cd serving
CI_TENSORFLOW_SUBMODULE_PATH=tensorflow tensorflow/tensorflow/tools/ci_build/ci_build.sh CPU bazel test //tensorflow_serving/...
```
注意：服务目录映射到容器中。 您可以在Docker容器之外开发（在您最喜爱的编辑器中），当您运行此构建时，它将随着您的更改而构建。