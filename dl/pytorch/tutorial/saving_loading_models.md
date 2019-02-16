1. torch.save   保存序列化对象到硬盘里。
2. torch.load   使用pickle的开箱工具，取出反序列化的pickled object 到内存里。
3. torch.nn.Module.load_state_dict 加载模型参数字典使用一个反序列化的state_dict

# state_dict
torch.nn.Module模型的可学习参数包含在model的参数里，可用model.parameters()读取。
state_dict是一个简化的python字典对象，映射每一次到它的参数tensor。
只有可学习参数有模型的state_dict的入口，包含optimizer的状态信息，使用的超参数也是。

Example:
```python
# Define model
class TheModelClass(nn.Module):
    def __init__(self):
        super(TheModelClass, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5)
        self.pool = nn.MaxPool2d(2, 2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = self.pool(F.relu(self.conv2(x)))
        x = x.view(-1, 16 * 5 * 5)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

# Initialize model
model = TheModelClass()

# Initialize optimizer
optimizer = optim.SGD(model.parameters(), lr=0.001, momentum=0.9)

# Print model's state_dict
print("Model's state_dict:")
for param_tensor in model.state_dict():
    print(param_tensor, "\t", model.state_dict()[param_tensor].size())

# Print optimizer's state_dict
print("Optimizer's state_dict:")
for var_name in optimizer.state_dict():
    print(var_name, "\t", optimizer.state_dict()[var_name])
```

输出
```
Model's state_dict:
conv1.weight     torch.Size([6, 3, 5, 5])
conv1.bias   torch.Size([6])
conv2.weight     torch.Size([16, 6, 5, 5])
conv2.bias   torch.Size([16])
fc1.weight   torch.Size([120, 400])
fc1.bias     torch.Size([120])
fc2.weight   torch.Size([84, 120])
fc2.bias     torch.Size([84])
fc3.weight   torch.Size([10, 84])
fc3.bias     torch.Size([10])

Optimizer's state_dict:
state    {}
param_groups     [{'lr': 0.001, 'momentum': 0.9, 'dampening': 0, 'weight_decay': 0, 'nesterov': False, 'params': [4675713712, 4675713784, 4675714000, 4675714072, 4675714216, 4675714288, 4675714432, 4675714504, 4675714648, 4675714720]}]
```


# Saving & Loading Model for Inferfence
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

当保存一个模型用于inference时，只需要保存训练模型的可学习参数。
用torch.save()保存模型的state_dict，会给你最大的灵活性去恢复模型，这是保存模型**推荐**的方法。
**记住**，在inference前，必须用model.eval()去设置droput和batch normalization层来为验证模式。


# Save/Load Entire Model
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
缺点是这种方法序列化数据束缚于专用的类和准确的目录结构。原因是pickle不保存模型类本身。

# Saving & Loading a General Checkpoint for Inference and/or Resuming Training
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

当保存一个通用的检查点时，能用于inference和恢复训练的方法，必须不只保存state_dict。
保存多个组件，组织一个，用torch.save()序列化这个字典。一个通用的pytorch的惯例是保存这些检查点为.tar文件扩展名

加载这些项，先初始化模型和优化器optimizer，然后使用torch.load()加载字典。
**记住**恢复训练，要调用 model.train()为确保这些层在训练模式。

# Saving Multiple Models in One File
Save:
'''python
torch.save({
            'modelA_state_dict': modelA.state_dict(),
            'modelB_state_dict': modelB.state_dict(),
            'optimizerA_state_dict': optimizerA.state_dict(),
            'optimizerB_state_dict': optimizerB.state_dict(),
            ...
            }, PATH)
'''
Load:
'''python
modelA = TheModelAClass(*args, **kwargs)
modelB = TheModelBClass(*args, **kwargs)
optimizerA = TheOptimizerAClass(*args, **kwargs)
optimizerB = TheOptimizerBClass(*args, **kwargs)

checkpoint = torch.load(PATH)
modelA.load_state_dict(checkpoint['modelA_state_dict'])
modelB.load_state_dict(checkpoint['modelB_state_dict'])
optimizerA.load_state_dict(checkpoint['optimizerA_state_dict'])
optimizerB.load_state_dict(checkpoint['optimizerB_state_dict'])

modelA.eval()
modelB.eval()
# - or -
modelA.train()
modelB.train()
'''


# Warmstarting Model Using Parameters from a Different Model
Save:
'''python
torch.save(modelA.state_dict(), PATH)
'''
Load:
'''python
modelB = TheModelBClass(*args, **kwargs)
modelB.load_state_dict(torch.load(PATH), strict=False)
'''
部分加载一个模型和加载部分模型是一个常见场景，尤其迁移学习或者训练一个复杂模型时。

不论是加载部分state_dict，它丢失了一些键，或者加载一个state_dict带有更多键，可以设置strict为False在load_state_dict()去忽略一些非匹配的键。

如果你想加载一些参数从一个层到另一个，但是一些keys不匹配，简单的改变state_dict中参数的名字。


# save&load model across devices
## Save on GPU, Load on CPU
Save:
'''python
torch.save(model.state_dict(), PATH)
'''
Load:
'''
device = torch.device('cpu')
model = TheModelClass(*args, **kwargs)
model.load_state_dict(torch.load(PATH, map_location=device))
'''

加载一个用GPU训练的模型到CPU上，传递torch.device('cpu')给map_location参数在torch.load()中。

## Save on GPU, Load on GPU
Save:
'''python
torch.save(model.state_dict(), PATH)
'''
Load:
'''python
device = torch.device("cuda")
model = TheModelClass(*args, **kwargs)
model.load_state_dict(torch.load(PATH))
model.to(device)
# Make sure to call input = input.to(device) on any input tensors that you feed to the model
'''

## Save on CPU, Load on GPU
Save:
'''python
torch.save(model.state_dict(), PATH)
'''
Load:
'''python
device = torch.device("cuda")
model = TheModelClass(*args, **kwargs)
model.load_state_dict(torch.load(PATH, map_location="cuda:0"))  # Choose whatever GPU device number you want
model.to(device)
# Make sure to call input = input.to(device) on any input tensors that you feed to the model
'''


## Saving torch.nn.DataParallel Models
Save:
'''python
torch.save(model.module.state_dict(), PATH)
'''
Load:
'''python
# Load to whatever device you want
'''
torch.nn.DataParallel is a model wrapper that enables parallel GPU utilization. To save a DataParallel model generically, save the model.module.state_dict(). This way, you have the flexibility to load the model any way you want to any device you want.



# 参考资料
[SAVING AND LOADING MODELS](https://pytorch.org/tutorials/beginner/saving_loading_models.html)