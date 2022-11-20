
import torch


class MyCell(torch.nn.Module):
    def __init__(self):
        super(MyCell, self).__init__()
        self.linear = torch.nn.Linear(4, 4)

    def forward(self, x, h):
        new_h = torch.tanh(self.linear(x) + h)
        return new_h, new_h

my_cell = MyCell()
print(my_cell)
x = torch.rand(3, 4)
h = torch.rand(3, 4)
print(my_cell(x, h))

'''
MyCell(
  (linear): Linear(in_features=4, out_features=4, bias=True)
)
(tensor([[ 0.4091,  0.9194,  0.6489,  0.6924],
        [-0.0770,  0.8848, -0.0645,  0.6007],
        [ 0.0601,  0.4428,  0.7904,  0.7802]], grad_fn=<TanhBackward>), tensor([[ 0.4091,  0.9194,  0.6489,  0.6924],
        [-0.0770,  0.8848, -0.0645,  0.6007],
        [ 0.0601,  0.4428,  0.7904,  0.7802]], grad_fn=<TanhBackward>))
'''

