
TorchScript is a way to create serializable and optimizable models from PyTorch code. Any TorchScript program can be saved from a Python process and loaded in a process where there is no Python dependency.

We provide tools to incrementally transition a model from a pure Python program to a TorchScript program that can be run independently from Python, such as in a standalone C++ program. This makes it possible to train models in PyTorch using familiar tools in Python and then export the model via TorchScript to a production environment where Python programs may be disadvantageous for performance and multi-threading reasons.

For a gentle introduction to TorchScript, see the Introduction to TorchScript tutorial.

For an end-to-end example of converting a PyTorch model to TorchScript and running it in C++, see the Loading a PyTorch Model in C++ tutorial.


