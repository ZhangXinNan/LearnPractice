from torchvision.models.resnet import BasicBlock, ResNet


def resnet10(**kwargs):
    model = ResNet(BasicBlock, [1, 1, 1, 1], **kwargs)
    return model
