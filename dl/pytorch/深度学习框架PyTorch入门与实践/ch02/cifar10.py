#_Author_:Monkey
#!/usr/bin/env python
#-*- coding:utf-8 -*-
import torch as t
import torchvision as tv
import torchvision.transforms as transforms
from torchvision.transforms import ToPILImage
import torch.utils.data as Data
import matplotlib.pyplot as plt
import numpy as np
import pylab
import torch.nn as nn
import torch.nn.functional as F
from torch import optim
from torch.autograd import Variable

def imshow(img):
    img = img / 2 + 0.5
    npimg = img.numpy()
    plt.imshow(np.transpose(npimg , (1 , 2 , 0)))
    pylab.show()

show = ToPILImage()	#可以把Tensor转成Image，方便可视化
transform = transforms.Compose([
	transforms.ToTensor(),	#转为Tensor
	transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5)),	#归一化
])
#训练集
trainset = tv.datasets.CIFAR10(root = '../data/',train=True,download=True,transform=transform)
trainloader = t.utils.data.DataLoader(trainset,batch_size=4,shuffle=True,num_workers=2)
#测试集
testset = tv.datasets.CIFAR10(	'../data/',train=False,	download=True,transform=transform)
testloader = Data.DataLoader(testset,batch_size=4,shuffle=False,num_workers=2)
classes = ('plane','car','bird','cat', 'deer','dog','frog','horse','ship','truck')
(data,label) = trainset[100]
print(classes[label])
# show((data+1)/2).resize((100,100))
imshow(data)




# dataiter = iter(trainloader,sentinel=None)
# images,labels = dataiter.next()  	#返回4张图片及标签
# print(''.join('%11s'%classes[labels[j]] for j in range(4)))
# show(tv.utils.make_grid((images+1)/2)).resize(400,100)

class Net(nn.Module):
	def __init__(self):
		super(Net,self).__init__()
		self.conv1 = nn.Conv2d(3,6,5)
		self.conv2 = nn.Conv2d(6,16,5)

		self.fc1 = nn.Linear(16*5*5,120)
		self.fc2 = nn.Linear(120,84)
		self.fc3 = nn.Linear(84,10)
	def forward(self,x):
		x = F.max_pool2d(F.relu(self.conv1(x)),(2,2))
		x = F.max_pool2d(F.relu(self.conv2(x)),2)
		x = x.view(x.size()[0],-1)
		x = F.relu(self.fc1(x))
		x = F.relu(self.fc2(x))
		x = self.fc3(x)
		return x
net = Net()

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(net.parameters(),lr = 0.001,momentum=0.9)
if __name__ == '__main__':
	for epoch in range(2):
		running_loss = 0.0

		for i ,data in enumerate(trainloader,0):
			imputs,labels = data
			imputs,labels = t.Tensor.float( Variable(imputs) ),\
							t.Tensor.float(Variable(label) )
            # 梯度清零
			optimizer.zero_grad()
            # forward + backward
			outputs = net(imputs)
			loss = criterion(outputs,labels)
			loss.backward()
            # 更新参数
			optimizer.step()

			running_loss += loss.data[0]
			if i%2000 == 1999:
				print('[%d,%5d] loss:%.3f'%(epoch+1,i+1,running_loss/2000))
				running_loss = 0.0
		print('Finish Training')