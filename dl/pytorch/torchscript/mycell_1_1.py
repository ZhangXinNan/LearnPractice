
import torch


class MyCell(torch.nn.Module):
    def __init__(self):
        super(MyCell, self).__init__()

    def forward(self, x, h):
        new_h = torch.tanh(x + h)
        return new_h

my_cell = MyCell()
print(my_cell)
x = torch.rand(3, 4)
h = torch.rand(3, 4)
print(my_cell(x, h))

'''
MyCell()
tensor([[0.8051, 0.8348, 0.7513, 0.6604],
        [0.8785, 0.9083, 0.9349, 0.7092],
        [0.9055, 0.7204, 0.1507, 0.5434]])
'''
