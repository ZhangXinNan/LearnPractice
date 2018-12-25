参考代码：
[pytorch/examples/imagenet](https://github.com/pytorch/examples/tree/master/imagenet)

# 错误1：
```
# (py36_pytorch)
python main.py \
>     -a resnet18 \
>     --lr 0.1 \
>     --dist-url 'tcp://127.0.0.1:23456' \
>     --dist-backend 'nccl' \
>     --multiprocessing-distributed \
>     --rank 0 \
>     /DATA/disk1/zhangxin/imagenet
Use GPU: 1 for training
Use GPU: 2 for training
Use GPU: 0 for training
=> creating model 'resnet18'
Use GPU: 3 for training
=> creating model 'resnet18'
Use GPU: 7 for training
=> creating model 'resnet18'
Use GPU: 4 for training
=> creating model 'resnet18'
Use GPU: 6 for training
=> creating model 'resnet18'
Use GPU: 5 for training
=> creating model 'resnet18'
=> creating model 'resnet18'
=> creating model 'resnet18'
Traceback (most recent call last):
  File "main.py", line 398, in <module>
    main()
  File "main.py", line 110, in main
    mp.spawn(main_worker, nprocs=ngpus_per_node, args=(ngpus_per_node, args))
  File "/home/work/anaconda3/envs/py36_pytorch/lib/python3.6/site-packages/torch/multiprocessing/spawn.py", line 167, in spawn
    while not spawn_context.join():
  File "/home/work/anaconda3/envs/py36_pytorch/lib/python3.6/site-packages/torch/multiprocessing/spawn.py", line 114, in join
    raise Exception(msg)
Exception:

-- Process 6 terminated with the following error:
Traceback (most recent call last):
  File "/home/work/anaconda3/envs/py36_pytorch/lib/python3.6/site-packages/torch/multiprocessing/spawn.py", line 19, in _wrap
    fn(i, *args)
  File "/DATA/disk1/zhangxin/github/examples/imagenet/main.py", line 151, in main_worker
    model = torch.nn.parallel.DistributedDataParallel(model, device_ids=[args.gpu])
  File "/home/work/anaconda3/envs/py36_pytorch/lib/python3.6/site-packages/torch/nn/parallel/distributed.py", line 215, in __init__
    self.broadcast_bucket_size)
  File "/home/work/anaconda3/envs/py36_pytorch/lib/python3.6/site-packages/torch/nn/parallel/distributed.py", line 377, in _dist_broadcast_coalesced
    dist._dist_broadcast_coalesced(self.process_group, tensors, buffer_size, False)
RuntimeError: NCCL error in: /opt/conda/conda-bld/pytorch_1544174967633/work/torch/lib/c10d/../c10d/NCCLUtils.hpp:39, invalid argument

```

解决方法：
```
添加--world-size参数
```
