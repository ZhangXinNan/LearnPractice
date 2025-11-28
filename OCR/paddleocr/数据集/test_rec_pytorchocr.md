

```bash
    -o Global.checkpoints=weights/ch_PP-OCRv3_rec/student.pth \



python tools/eval.py \
    -c configs/rec/PP-OCRv3/ch_PP-OCRv3_rec_distillation.yml \
    -o Global.checkpoints=weights/ch_PP-OCRv3_rec/best_accuracy.pth \
    Global.use_gpu=False \
    Eval.dataset.data_dir=/Users/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition \
    Eval.dataset.label_file_list='[/Users/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/train_1000.txt]'
```

```
Traceback (most recent call last):
  File "/Users/zhangxin/github/PytorchOCR/tools/eval.py", line 44, in <module>
    main()
  File "/Users/zhangxin/github/PytorchOCR/tools/eval.py", line 29, in main
    trainer = Trainer(cfg, mode='eval')
  File "/Users/zhangxin/github/PytorchOCR/torchocr/engine/trainer.py", line 103, in __init__
    self.status = load_ckpt(self.model, self.cfg, self.optimizer, self.lr_scheduler)
  File "/Users/zhangxin/github/PytorchOCR/torchocr/utils/ckpt.py", line 57, in load_ckpt
    logger.info(f"resume from checkpoint: {checkpoints} (epoch {checkpoint['epoch']})")
KeyError: 'epoch'
```

```bash
python tools/eval.py \
    -c configs/rec/PP-OCRv3/ch_PP-OCRv3_rec.yml \
    -o Global.checkpoints=weights/ch_PP-OCRv3_rec/student.pth \
    Global.use_gpu=False \
    Eval.dataset.data_dir=/Users/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition \
    Eval.dataset.label_file_list='[/Users/zhangxin/data_public/OCR/3_Chinese-Street-View-Text-Recognition/train_1000.txt]'
```


```
Traceback (most recent call last):
  File "/Users/zhangxin/github/PytorchOCR/tools/eval.py", line 44, in <module>
    main()
  File "/Users/zhangxin/github/PytorchOCR/tools/eval.py", line 29, in main
    trainer = Trainer(cfg, mode='eval')
  File "/Users/zhangxin/github/PytorchOCR/torchocr/engine/trainer.py", line 103, in __init__
    self.status = load_ckpt(self.model, self.cfg, self.optimizer, self.lr_scheduler)
  File "/Users/zhangxin/github/PytorchOCR/torchocr/utils/ckpt.py", line 57, in load_ckpt
    logger.info(f"resume from checkpoint: {checkpoints} (epoch {checkpoint['epoch']})")
KeyError: 'epoch'
```



