import time
import os
import torch
import torch.utils.data
import torchvision
import visdom
import numpy as np
# import models.resnet10
import resnet10
from imagenet_data import ImageNetData


DISPLAY = 50
EPOCH = 300
LR = 0.05
iter_train_loss = []
iter_index = 0
epoch_train_loss = []
epoch_val_loss = []
epoch_val_error = []

viz = visdom.Visdom(port=10001)
session = time.strftime('%Y%m%d-%H-%M-%S', time.localtime(time.time()))
model_path = os.path.join('check_points/{}'.format(session))
if not os.path.exists(model_path):
    os.makedirs(model_path)

win_opts = {
    'train': {'title': 'Train Loss', 'xlabel': 'Epoch', 'ylabel': 'Loss'},
    'val': {'title': 'Val Loss', 'xlabel': 'Epoch', 'ylabel': 'Loss'},
    'val_precision': {'title': 'Val Error', 'xlabel': 'Epoch', 'ylabel': 'Error', 'legend': ['top1 error', 'top5 error']},
    'iter': {'title': "Iter Loss", 'xlabel': 'Iter', 'ylabel': 'Loss'},
    'epoch': {'title': "Epoch Loss", 'xlabel': 'Epoch', 'ylabel': 'Loss', 'legend': ['train loss', 'val loss']}
}

train_win = None
val_win = None
val_precision_win = None
iter_win = None
epoch_win = None


def calc_precision(pred, label):
    t1 = torch.topk(pred, 1)[-1]
    t5 = torch.topk(pred, 5)[-1]
    mask_1 = torch.eq(t1, label.view(-1, 1))
    mask_5 = torch.eq(t5, label.view(-1, 1))
    t1_error = 1 - len(t1[mask_1]) / len(label)
    t5_error = 1 - len(t5[mask_5]) / len(label)
    return t1_error, t5_error


def train(epoch, model, dataloader, loss_F, optim):
    model.train()
    total_loss = 0.
    batch_loss = 0.
    start = time.time()
    for index, (img, label) in enumerate(dataloader):
        # print(index )
        # img, label = datas['img'], datas['label']
        if torch.cuda.is_available():
            img = img.cuda()
            label = label.cuda()
        pred = model(img)
        # label = label.flatten()
        loss = loss_F(pred, label)
        total_loss += loss.data.item()
        batch_loss += loss.data.item()
        optim.zero_grad()
        loss.backward()
        optim.step()
        if (index + 1) % DISPLAY == 0:
            batch_loss /= DISPLAY
            global iter_index
            t1_e, t5_e = calc_precision(pred, label)
            iter_train_loss.append(batch_loss)
            print("[train] epoch: {0}, loss: {1}, top1 error: {2}, top5 error: {3}, LR: {4}, time: {5}".format(
                epoch, batch_loss, t1_e, t5_e, LR, (time.time() - start)))
            if viz and viz.check_connection():
                global iter_win
                iter_win = viz.line(
                    iter_train_loss, list(range(0, (iter_index + 1)*DISPLAY, DISPLAY)),
                    win=iter_win, name='train loss', opts=win_opts['iter'], env=session
                )
            batch_loss = 0.
            iter_index += 1

    avg_loss = total_loss / len(dataloader)
    epoch_train_loss.append(avg_loss)
    if viz and viz.check_connection():
        global train_win
        train_win = viz.line(
            epoch_train_loss, list(range(epoch + 1)),
            win=train_win, name='train_loss',
            opts=win_opts['train'], env=session)

    with open(model_path + '/log.txt', 'a+') as f:
        f.write("[train] epoch: {0}, loss{1}, LR: {2}\n".format(
            epoch, avg_loss, LR))


def test(epoch, model, dataloader, loss_F):
    start = time.time()
    model.train()
    total_loss = 0.
    t1_error = 0.
    t5_error = 0.
    for index, (data, label) in enumerate(dataloader):
        if torch.cuda.is_available():
            data = data.cuda()
            label = label.cuda()
        pred = model(data)
        loss = loss_F(pred, label)
        total_loss += loss.data.item()
        t1_e, t5_e = calc_precision(pred, label)
        t1_error += t1_e
        t5_error += t5_e
    t1_error /= len(dataloader)
    t5_error /= len(dataloader)
    epoch_val_error.append([t1_error, t5_error])
    avg_loss = total_loss / len(dataloader)
    epoch_val_loss.append(avg_loss)

    print("[val] epoch: {0}, loss: {1}, top1 error: {2}, top5 error: {3}, LR: {4}, time: {5}".format(
        epoch, avg_loss, t1_error, t5_error, LR, (time.time() - start)))

    if viz and viz.check_connection():
        global val_win, val_precision_win
        val_win = viz.line(
            epoch_val_loss, list(range(epoch + 1)),
            win=val_win, name='val_loss',
            opts=win_opts['val'], env=session)
        val_precision_win = viz.line(
            epoch_val_error, list(range(epoch+1)), win=val_precision_win, name='error', opts=win_opts['val_precision'],
            env=session
        )
        # val_precision_win = viz.line(
        #     epoch_val_t5, list(range(epoch+1)), win=val_precision_win, name='top 5', opts=win_opts['val_precision'],
        #     env=session
        # )
    with open(model_path + '/log.txt', 'a+') as f:
        f.write("[val] epoch: {0}, loss{1}, t1_error: {2}, t5_error: {3}, LR: {4}\n".format(
            epoch, avg_loss, t1_error, t5_error, LR))


if "__main__" == __name__:
    resnet10_model = resnet10.resnet10()
    transforms = torchvision.transforms.Compose([
        torchvision.transforms.Resize(224),
        torchvision.transforms.CenterCrop((224, 224)),
        torchvision.transforms.ToTensor()
    ])
    if torch.cuda.is_available():
        resnet10_model = resnet10_model.cuda()
    resnet10_model = torch.nn.DataParallel(resnet10_model)
    train_set = ImageNetData('../train_zx.txt', transforms=transforms)
    train_loader = torch.utils.data.DataLoader(train_set, batch_size=128, shuffle=True, num_workers=16, drop_last=True)
    test_set = ImageNetData('../val_zx.txt', transforms=transforms)
    test_loader = torch.utils.data.DataLoader(test_set, batch_size=128, shuffle=False, num_workers=16)

    criterion = torch.nn.CrossEntropyLoss()
    if torch.cuda.is_available():
        criterion = criterion.cuda()
    optim = torch.optim.SGD(resnet10_model.parameters(), lr=LR, momentum=0.9, weight_decay=0.0001)
    lr_scheduler = torch.optim.lr_scheduler.StepLR(optim, 10, 0.1)
    for epoch in range(EPOCH):
        lr_scheduler.step()
        LR = lr_scheduler.get_lr()[0]
        train(epoch, resnet10_model, train_loader, criterion, optim)
        test(epoch, resnet10_model, test_loader, criterion)
        if viz and viz.check_connection():
            epoch_win = viz.line(
                np.array([epoch_train_loss, epoch_val_loss]).transpose(1, 0), list(range(epoch + 1)),
                win=epoch_win, opts=win_opts['epoch'], env=session)
        torch.save({
            'session': session,
            'epoch': epoch + 1,
            'model': resnet10_model.module.state_dict(),
            'optimizer': optim.state_dict(),
            'scheduler': lr_scheduler.state_dict(),
        }, "{0}/epoch_{1}.pth".format(model_path, epoch))
