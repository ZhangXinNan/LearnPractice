


```bash
Traceback (most recent call last):
  File "D:/gitlab/CarRecognition/Train/pytorch/train_car_test.py", line 349, in <module>
    main(get_args())
  File "D:/gitlab/CarRecognition/Train/pytorch/train_car_test.py", line 335, in main
    model_ft, val_acc_history, val_loss_history, train_acc_history, train_loss_history = train_model(model_ft, dataloaders_dict, criterion, optimizer_ft, num_epochs=num_epochs, is_inception=(model_name=="inception"))
  File "D:/gitlab/CarRecognition/Train/pytorch/train_car_test.py", line 152, in train_model
    torch.save(best_model_wts.state_dict(), _TMP + 'ft_{}_{}_{}.pth'.format(model_name, best_epoch, best_acc))
AttributeError: 'collections.OrderedDict' object has no attribute 'state_dict'
```

