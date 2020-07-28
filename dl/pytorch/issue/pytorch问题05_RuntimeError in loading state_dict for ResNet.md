

# 1 问题
```bash
RuntimeError: Error(s) in loading state_dict for ResNet:
        Missing key(s) in state_dict: "layer1.0.conv3.weight", "layer1.0.bn3.weight", 
```

# 2 解决办法
## 2.1 load_state_dict(, strict=False)
```bash
RuntimeError: Error(s) in loading state_dict for ResNet:
        size mismatch for layer1.0.conv1.weight: copying a param with shape torch.Size([64, 64, 3, 3]) from checkpoint, the shape in current model is torch.Size([64, 64, 1, 1]).
```

## 2.2 