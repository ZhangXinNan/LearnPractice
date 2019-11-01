

```bash
D:\data_autohome\autoimg1\97.191.3455\1002214.1.100056478.jpg 49 392 994 689 (945, 297) RGB
Traceback (most recent call last):
  File "D:\gitlab\CarRecognition\Train\pytorch\CarDataset.py", line 75, in __getitem__
    image = self.transform(image)
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch13\lib\site-packages\torchvision\transforms\transforms.py", line 61, in __call__
    img = t(img)
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch13\lib\site-packages\torchvision\transforms\transforms.py", line 92, in __call__
    return F.to_tensor(pic)
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch13\lib\site-packages\torchvision\transforms\functional.py", line 99, in to_tensor
    return img.float().div(255)
RuntimeError: [enforce fail at ..\c10\core\CPUAllocator.cpp:72] data. DefaultCPUAllocator: not enough memory: you tried to allocate 602112 bytes. Buy new RAM!
```