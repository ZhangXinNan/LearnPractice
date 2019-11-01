```bash
Traceback (most recent call last):
  File "D:/gitlab/CarRecognition/Train/pytorch/train_car.py", line 318, in <module>
    if __name__ == '__main__':
  File "D:/gitlab/CarRecognition/Train/pytorch/train_car.py", line 304, in main
    # Train and evaluate
  File "D:/gitlab/CarRecognition/Train/pytorch/train_car.py", line 55, in train_model
    # Iterate over data.
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch13\lib\site-packages\torch\utils\data\dataloader.py", line 819, in __next__
    return self._process_data(data)
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch13\lib\site-packages\torch\utils\data\dataloader.py", line 846, in _process_data
    data.reraise()
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch13\lib\site-packages\torch\_utils.py", line 385, in reraise
    raise self.exc_type(msg)
RuntimeError: Caught RuntimeError in DataLoader worker process 0.
Original Traceback (most recent call last):
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch13\lib\site-packages\torch\utils\data\_utils\worker.py", line 178, in _worker_loop
    data = fetcher.fetch(index)
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch13\lib\site-packages\torch\utils\data\_utils\fetch.py", line 47, in fetch
    return self.collate_fn(data)
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch13\lib\site-packages\torch\utils\data\_utils\collate.py", line 79, in default_collate
    return [default_collate(samples) for samples in transposed]
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch13\lib\site-packages\torch\utils\data\_utils\collate.py", line 79, in <listcomp>
    return [default_collate(samples) for samples in transposed]
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch13\lib\site-packages\torch\utils\data\_utils\collate.py", line 53, in default_collate
    storage = elem.storage()._new_shared(numel)
  File "D:\ProgramData\Anaconda3\envs\py36_pytorch13\lib\site-packages\torch\storage.py", line 128, in _new_shared
    return cls._new_using_filename(size)
RuntimeError: Couldn't open shared file mapping: <torch_22884_2321048452>, error code: <1455>
```


