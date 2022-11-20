
# Serve a Model in 3 Easy Steps
```bash
# Step 1: Create the example model repository 
git clone -b r22.10 https://github.com/triton-inference-server/server.git
cd server/docs/examples
./fetch_models.sh
```

# Step 2: Launch triton from the NGC Triton container
```bash
# 奖model_repository映射到容器内的/model目录
docker run --gpus=1 --rm --net=host -v ${PWD}/model_repository:/models nvcr.io/nvidia/tritonserver:22.10-py3 tritonserver --model-repository=/models
```

```
I1109 07:53:20.676812 1 server.cc:590] 
+-------------+-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Backend     | Path                                                            | Config                                                                                                                                                        |
+-------------+-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
| tensorflow  | /opt/tritonserver/backends/tensorflow2/libtriton_tensorflow2.so | {"cmdline":{"auto-complete-config":"true","min-compute-capability":"6.000000","backend-directory":"/opt/tritonserver/backends","default-max-batch-size":"4"}} |
| onnxruntime | /opt/tritonserver/backends/onnxruntime/libtriton_onnxruntime.so | {"cmdline":{"auto-complete-config":"true","min-compute-capability":"6.000000","backend-directory":"/opt/tritonserver/backends","default-max-batch-size":"4"}} |
+-------------+-----------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

I1109 07:53:20.676901 1 server.cc:633] 
+----------------------+---------+--------+
| Model                | Version | Status |
+----------------------+---------+--------+
| densenet_onnx        | 1       | READY  |
| inception_graphdef   | 1       | READY  |
| simple               | 1       | READY  |
| simple_dyna_sequence | 1       | READY  |
| simple_identity      | 1       | READY  |
| simple_int8          | 1       | READY  |
| simple_sequence      | 1       | READY  |
| simple_string        | 1       | READY  |
+----------------------+---------+--------+

I1109 07:53:20.685349 1 metrics.cc:864] Collecting metrics for GPU 0: Quadro RTX 5000 with Max-Q Design
I1109 07:53:20.685511 1 metrics.cc:757] Collecting CPU metrics
I1109 07:53:20.685644 1 tritonserver.cc:2264] 
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Option                           | Value                                                                                                                                                                                                |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| server_id                        | triton                                                                                                                                                                                               |
| server_version                   | 2.27.0                                                                                                                                                                                               |
| server_extensions                | classification sequence model_repository model_repository(unload_dependents) schedule_policy model_configuration system_shared_memory cuda_shared_memory binary_tensor_data statistics trace logging |
| model_repository_path[0]         | /models                                                                                                                                                                                              |
| model_control_mode               | MODE_NONE                                                                                                                                                                                            |
| strict_model_config              | 0                                                                                                                                                                                                    |
| rate_limit                       | OFF                                                                                                                                                                                                  |
| pinned_memory_pool_byte_size     | 268435456                                                                                                                                                                                            |
| cuda_memory_pool_byte_size{0}    | 67108864                                                                                                                                                                                             |
| response_cache_byte_size         | 0                                                                                                                                                                                                    |
| min_supported_compute_capability | 6.0                                                                                                                                                                                                  |
| strict_readiness                 | 1                                                                                                                                                                                                    |
| exit_timeout                     | 30                                                                                                                                                                                                   |
+----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

I1109 07:53:20.686425 1 grpc_server.cc:4819] Started GRPCInferenceService at 0.0.0.0:8001
I1109 07:53:20.686652 1 http_server.cc:3474] Started HTTPService at 0.0.0.0:8000
I1109 07:53:20.729274 1 http_server.cc:181] Started Metrics Service at 0.0.0.0:8002
W1109 07:53:21.687930 1 metrics.cc:603] Unable to get power limit for GPU 0. Status:Success, value:0.000000
W1109 07:53:22.688967 1 metrics.cc:603] Unable to get power limit for GPU 0. Status:Success, value:0.000000
W1109 07:53:23.691835 1 metrics.cc:603] Unable to get power limit for GPU 0. Status:Success, value:0.000000
```

# Step 3: Sending an Inference Request 
```bash
# In a separate console, launch the image_client example from the NGC Triton SDK container
docker run -it --rm --net=host nvcr.io/nvidia/tritonserver:22.10-py3-sdk

/workspace/install/bin/image_client -m densenet_onnx -c 3 -s INCEPTION /workspace/images/mug.jpg

# Inference should return the following
Image '/workspace/images/mug.jpg':
    15.346230 (504) = COFFEE MUG
    13.224326 (968) = CUP
    10.422965 (505) = COFFEEPOT

/workspace/install/bin/image_client -m densenet_onnx -c 3 -b 1 -s INCEPTION /workspace/images/mug.jpg
```