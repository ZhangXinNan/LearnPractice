CPU下使用
```
def crnnSource(path):
    alphabet = keys.alphabet
    converter = util.strLabelConverter(alphabet)
    model = crnn.CRNN(32, 1, len(alphabet)+1, 256, 1)
    if torch.cuda.is_available():
        model = model.cuda()
    # path = './crnn/samples/netCRNN63.pth'
    # model.load_state_dict(torch.load(path))
    if torch.cuda.is_available():
        model.load_state_dict(torch.load(path))
    else:
        model.load_state_dict(torch.load(path, map_location=lambda storage, location: storage))
    
    return model,converter


def crnn_line_rec(model,converter,image):
    scale = image.size[1]*1.0 / 32
    w = image.size[0] / scale
    w = int(w)
    #print(w)

    transformer = dataset.resizeNormalize((w, 32))
    image = transformer(image)
    if torch.cuda.is_available():
        image = image.cuda()
    image = image.view(1, *image.size())
    image = Variable(image)
    model.eval()
    preds = model(image)
    _, preds = preds.max(2)
    # RuntimeError: dimension out of range (expected to be in range of [-2, 1], but got 2)
    # preds = preds.squeeze(2)
    preds = preds.transpose(1, 0).contiguous().view(-1)
    preds_size = Variable(torch.IntTensor([preds.size(0)]))
    raw_pred = converter.decode(preds.data, preds_size.data, raw=True)
    sim_pred = converter.decode(preds.data, preds_size.data, raw=False)
    #print('%-20s => %-20s' % (raw_pred, sim_pred))
    # print(sim_pred)
    return sim_pred
```