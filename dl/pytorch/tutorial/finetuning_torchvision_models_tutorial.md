

# 输入
1. model_name 模型的名字，
```
[resnet, alexnet, vgg, squeezenet, densenet, inception]
```

2. num_classes 数据集中类别的数量
3. batch_size 
4. num_epochs 
5. feature_extract 微调或者特征提取
如果feature_extract=False，模型是微调，所有参数都要更新；
否则，只有最后一层被更新，其他层固定。
```
# Top level data directory. Here we assume the format of the directory conforms
#   to the ImageFolder structure
data_dir = "./data/hymenoptera_data"

# Models to choose from [resnet, alexnet, vgg, squeezenet, densenet, inception]
model_name = "squeezenet"

# Number of classes in the dataset
num_classes = 2

# Batch size for training (change depending on how much memory you have)
batch_size = 8

# Number of epochs to train for
num_epochs = 15

# Flag for feature extracting. When False, we finetune the whole model,
#   when True we only update the reshaped layer params
feature_extract = True
```



