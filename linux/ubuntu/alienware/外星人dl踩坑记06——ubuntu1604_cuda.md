[Ubuntu16.04 install CUDA 9.0 + cuDNN 7.0.5](https://medium.com/cs-note/ubuntu16-04-install-cuda-9-0-cudnn-7-0-5-80c53404516c)

[Install CUDA 9.0 and cuDNN 7.0 for TensorFlow/PyTorch (GPU) on Ubuntu 16.04](https://medium.com/@zhanwenchen/install-cuda-and-cudnn-for-tensorflow-gpu-on-ubuntu-79306e4ac04e)


# Step 0 Noveau drivers
## 1 Press ctrl+alt+F1
## 2 Create a file: /etc/modprobe.d/blacklist-nouveau.conf
```
sudo vi /etc/modprobe.d/blacklist-nouveau.conf
```

## 3 Put the following in the file
```
blacklist nouveau
options nouveau modeset=0
```

## 4 update-initramfs
```
sudo update-initramfs –u
```

## 5. reboot
```
sudo reboot
```
## 6. After reboot
```
lsmod | grep nouveau
```
And there is nothing output. If you output something, you need to check the step.





```
./cuda_9.0.176_384.81_linux_.run --extract=$HOME

sudo ./cuda-linux.9.0.176-22781540.run

sudo ./cuda-samples.9.0.176-22781540-linux.run
```

```
please make sure that
- PATH includes /usr/local/cuda-9.0/bin
- LD_LIBRARY_PATH includes /usr/local/cuda-9.0/lib64, or, add /usr/local/cuda-9.0/lib64 to /etc/ld.so.conf and run ldconfig as root
```


### 出现问题
```
CUDA driver version is insufficient for CUDA runtime version
```

