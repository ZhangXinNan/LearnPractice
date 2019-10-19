
[SAVING AND LOADING MODELS](https://pytorch.org/tutorials/beginner/saving_loading_models.html)


* torch.save 保存一个序列化对象到硬盘里。调用了python的pickle工具来序列化。
* torch.load 反序列化到内存中。
* torch.nn.Module.load_state_dict 加载一个模型参数字典，使用反序列化的state_dict。

# 1 state_dict
torch.nn.Module 的可学习参数包含在 model.parameters()。
state_dict 是一个简化 的python dictionary对象，映射每个层到它的参数tensor。
```python
# Print model's state_dict
print("Model's state_dict:")
for param_tensor in model.state_dict():
    print(param_tensor, "\t", model.state_dict()[param_tensor].size())

# Print optimizer's state_dict
print("Optimizer's state_dict:")
for var_name in optimizer.state_dict():
    print(var_name, "\t", optimizer.state_dict()[var_name])
```

# 2 Saving & Loading Model for Inference
Save:
```python
torch.save(model.state_dict(), PATH)
```

Load:
```python
model = TheModelClass(*args, **kwargs)
model.load_state_dict(torch.load(PATH))
model.eval()
```


用于推理时，只需要保存 learned parameters。
用于推理前，需要调用model.eval()来设置dropout、batch normalization层。


# 3 Save/Load Entire Model
Save:
```python
torch.save(model, PATH)
```
Load:
```python
# Model class must be defined somewhere
model = torch.load(PATH)
model.eval()
```



# 4 Saving & Loading a General Checkpoint for Inference and/or Resuming Training
Save:
```python
torch.save({
            'epoch': epoch,
            'model_state_dict': model.state_dict(),
            'optimizer_state_dict': optimizer.state_dict(),
            'loss': loss,
            ...
            }, PATH)
```

Load:
```python
model = TheModelClass(*args, **kwargs)
optimizer = TheOptimizerClass(*args, **kwargs)

checkpoint = torch.load(PATH)
model.load_state_dict(checkpoint['model_state_dict'])
optimizer.load_state_dict(checkpoint['optimizer_state_dict'])
epoch = checkpoint['epoch']
loss = checkpoint['loss']

model.eval()
# - or -
model.train()
```