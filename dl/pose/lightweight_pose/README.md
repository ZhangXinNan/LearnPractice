
```bash
conda create -n py311_pose python=3.11

conda activate py311_pose

pip install torch torchvision

pycocotools==2.0.11
opencv-python==5.0.0.93
numpy==2.4.6
```



```bash
# python demo.py --checkpoint-path <path_to>/checkpoint_iter_370000.pth --video 0

python demo.py --checkpoint-path ./checkpoint_iter_370000.pth --video 0 --cpu

python demo.py --checkpoint-path ./checkpoint_iter_370000.pth --images bus.jpg --cpu
```



