The following figure shows the Triton Inference Server high-level architecture. The model repository is a file-system based repository of the models that Triton will make available for inferencing. Inference requests arrive at the server via either HTTP/REST or GRPC or by the C API and are then routed to the appropriate per-model scheduler. Triton implements multiple scheduling and batching algorithms that can be configured on a model-by-model basis. Each model's scheduler optionally performs batching of inference requests and then passes the requests to the backend corresponding to the model type. The backend performs inferencing using the inputs provided in the batched requests to produce the requested outputs. The outputs are then returned.

Triton supports a backend C API that allows Triton to be extended with new functionality such as custom pre- and post-processing operations or even a new deep-learning framework.

The models being served by Triton can be queried and controlled by a dedicated model management API that is available by HTTP/REST or GRPC protocol, or by the C API.

Readiness and liveness health endpoints and utilization, throughput and latency metrics ease the integration of Triton into deployment framework such as Kubernetes.


下图显示了 Triton 推理服务器的高级架构。模型存储库是基于文件系统的模型存储库，Triton 将使其可用于推理。推理请求通过 HTTP/REST 或 GRPC 或 C API 到达服务器，然后路由到适当的每个模型调度程序。 Triton 实现了多种调度和批处理算法，可以在逐个模型的基础上进行配置。每个模型的调度程序可选地执行推理请求的批处理，然后将请求传递到与模型类型对应的后端。后端使用批处理请求中提供的输入执行推理，以生成请求的输出。然后返回输出。

Triton 支持后端 C API，允许使用新功能扩展 Triton，例如自定义预处理和后处理操作，甚至是新的深度学习框架。

Triton 服务的模型可以通过 HTTP/REST 或 GRPC 协议或 C API 可用的专用模型管理 API 进行查询和控制。

就绪性和活跃性健康端点以及利用率、吞吐量和延迟指标简化了 Triton 与 Kubernetes 等部署框架的集成。

![](arch.jpg)



# 1 Concurrent Model Execution
The Triton architecture allows multiple models and/or multiple instances of the same model to execute in parallel on the same system. The system may have zero, one, or many GPUs. The following figure shows an example with two models; model0 and model1. Assuming Triton is not currently processing any request, when two requests arrive simultaneously, one for each model, Triton immediately schedules both of them onto the GPU and the GPU’s hardware scheduler begins working on both computations in parallel. Models executing on the system's CPU are handled similarly by Triton except that the scheduling of the CPU threads execution each model is handled by the system's OS.

![Triton Mult-Model Execution Diagram](multi_model_exec.png)

By default, if multiple requests for the same model arrive at the same time, Triton will serialize their execution by scheduling only one at a time on the GPU, as shown in the following figure.

![Triton Mult-Model Serial Execution Diagram](multi_model_serial_exec.png)

Triton provides a model configuration option called instance-group that allows each model to specify how many parallel executions of that model should be allowed. Each such enabled parallel execution is referred to as an instance. By default, Triton gives each model a single instance for each available GPU in the system. By using the instance_group field in the model configuration, the number of execution instances for a model can be changed. The following figure shows model execution when model1 is configured to allow three instances. As shown in the figure, the first three model1 inference requests are immediately executed in parallel. The fourth model1 inference request must wait until one of the first three executions completes before beginning.

![Triton Mult-Model Parallel Execution Diagram](multi_model_parallel_exec.png)

# 2 Models And Schedulers
Triton supports multiple scheduling and batching algorithms that can be selected independently for each model. This section describes stateless, stateful and ensemble models and how Triton provides schedulers to support those model types. For a given model, the selection and configuration of the scheduler is done with the model's configuration file.

## 2.1 Stateless Models
With respect to Triton's schedulers, a stateless model does not maintain state between inference requests. Each inference performed on a stateless model is independent of all other inferences using that model.

Examples of stateless models are CNNs such as image classification and object detection. The default scheduler or dynamic batcher can be used as the scheduler for these stateless models.

RNNs and similar models which do have internal memory can be stateless as long as the state they maintain does not span inference requests. For example, an RNN that iterates over all elements in a batch is considered stateless by Triton if the internal state is not carried between batches of inference requests. The default scheduler can be used for these stateless models. The dynamic batcher cannot be used since the model is typically not expecting the batch to represent multiple inference requests.

## 2.2 Stateful Models
With respect to Triton's schedulers, a stateful model does maintain state between inference requests. The model is expecting multiple inference requests that together form a sequence of inferences that must be routed to the same model instance so that the state being maintained by the model is correctly updated. Moreover, the model may require that Triton provide control signals indicating, for example, the start and end of the sequence.

The sequence batcher must be used for these stateful models. As explained below, the sequence batcher ensures that all inference requests in a sequence get routed to the same model instance so that the model can maintain state correctly. The sequence batcher also communicates with the model to indicate when a sequence is starting, when a sequence is ending, when a sequence has an inference request ready for execution, and the correlation ID of the sequence.

When making inference requests for a stateful model, the client application must provide the same correlation ID to all requests in a sequence, and must also mark the start and end of the sequence. The correlation ID allows Triton to identify that the requests belong to the same sequence.


