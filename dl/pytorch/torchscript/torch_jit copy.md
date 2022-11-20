

TorchScript 是一种从 PyTorch 代码创建可序列化和可优化模型的方法。 任何 TorchScript 程序都可以从 Python 进程中保存并加载到没有 Python 依赖项的进程中。

我们提供工具将模型从纯 Python 程序逐步转换为可以独立于 Python 运行的 TorchScript 程序，例如在独立的 C++ 程序中。 这使得使用 Python 中熟悉的工具在 PyTorch 中训练模型成为可能，然后通过 TorchScript 将模型导出到生产环境中，其中 Python 程序可能由于性能和多线程原因而处于不利地位。

有关 TorchScript 的简要介绍，请参阅 TorchScript 简介教程。

有关将 PyTorch 模型转换为 TorchScript 并在 C++ 中运行的端到端示例，请参阅在 C++ 中加载 PyTorch 模型教程。

