#_Author_:Monkey
#!/usr/bin/env python
#-*- coding:utf-8 -*-
# import torch
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

# show = ToPILImage()	#可以把Tensor转成Image，方便可视化
classes = ('plane','car','bird','cat', 'deer','dog','frog','horse','ship','truck')
# (data,label) = trainset[100]
# print(classes[label])
# show((data+1)/2).resize((100,100))
# imshow(data)



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


def test(net, testloader, device):
	correct = 0
	total = 0
	with t.no_grad():
		for inputs, labels in testloader:
			if t.cuda.is_available():
				inputs, labels = inputs.to(device), labels.to(device)
			outputs = net(inputs)
			_, predicted = t.max(outputs.data, 1)
			total += labels.size(0)
			correct += (predicted == labels).sum().item()
	print('Accuracy of the network on the 10000 test images: %d %%' % (100 * correct / total))


def test_all(net, testloader, device):
	class_correct = list(0. for i in range(10))
	class_total = list(0. for i in range(10))
	with t.no_grad():
		for inputs, labels in testloader:
			if t.cuda.is_available():
				inputs, labels = inputs.to(device), labels.to(device)
			outputs = net(inputs)
			_, predicted = t.max(outputs, 1)
			c = (predicted == labels).squeeze()
			for i in range(4):
				label = labels[i]
				class_correct[label] += c[i].item()
				class_total[label] += 1

	for i in range(10):
		print('Accuracy of %5s : %2d %%' % (
			classes[i], 100 * class_correct[i] / class_total[i]))


def main():
	# device = t.device("cuda:0" if t.cuda.is_available() else "cpu")
	device = t.device("cpu")
	# Assuming that we are on a CUDA machine, this should print a CUDA device:
	print(device)

	transform = transforms.Compose([
			transforms.ToTensor(),	#转为Tensor
			transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5)),	#归一化
		])
	#测试集
	testset = tv.datasets.CIFAR10(root='../data/',train=False,	download=True,transform=transform)
	testloader = Data.DataLoader(testset,batch_size=4,shuffle=False,num_workers=1)
	#训练集
	trainset = tv.datasets.CIFAR10(root = '../data/',train=True,download=True,transform=transform)
	trainloader = t.utils.data.DataLoader(trainset,batch_size=4,shuffle=True,num_workers=1)

	net = Net()
	if t.cuda.is_available():
		net.to(device=device)

	criterion = nn.CrossEntropyLoss()
	optimizer = optim.SGD(net.parameters(),lr = 0.001,momentum=0.9)

	for epoch in range(1):
		running_loss = 0.0

		for i ,data in enumerate(trainloader,0):
			inputs,labels = data
			if t.cuda.is_available():
				inputs, labels = inputs.to(device), labels.to(device)
			# inputs, labels = Variable(inputs), Variable(labels)
			# inputs,labels = t.Tensor.float( Variable(inputs) ), t.Tensor.float(Variable(labels) )
            # 梯度清零
			optimizer.zero_grad()
            # forward + backward
			outputs = net(inputs)
			loss = criterion(outputs,labels)
			loss.backward()
            # 更新参数
			optimizer.step()

			running_loss += loss.item() # loss.data[0]
			if i%2000 == 1999:
				print('[%d,%5d] loss:%.3f'%(epoch+1,i+1,running_loss/2000))
				running_loss = 0.0
		test(net, testloader, device)
	print('Finish Training')
	t.save(net.state_dict(), './cifar_net.pth')
	test_all(net, testloader, device)


if __name__ == '__main__':
	main()