
import torch as t
import visdom

# 新建一个连接客户端
# 指定env为test1，默认端口为8097，host是localhost
vis = visdom.Visdom(env=u'test1')

x = t.arange(1, 30, 0.01)
y = t.sin(x)

vis.line(X=x, Y=y, win='sinx', opts={'title': 'y=sin(x)'})


