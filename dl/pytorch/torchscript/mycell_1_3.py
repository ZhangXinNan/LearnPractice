
import torch


class MyDecisionGate(torch.nn.Module):
    def forward(self, x):
        if x.sum() > 0:
            return x
        else:
            return -x

class MyCell(torch.nn.Module):
    def __init__(self):
        super(MyCell, self).__init__()
        self.dg = MyDecisionGate()
        self.linear = torch.nn.Linear(4, 4)

    def forward(self, x, h):
        new_h = torch.tanh(self.dg(self.linear(x)) + h)
        return new_h, new_h

my_cell = MyCell()
print(my_cell)
x = torch.rand(3, 4)
h = torch.rand(3, 4)
print(my_cell(x, h))


'''
MyCell(
  (dg): MyDecisionGate()
  (linear): Linear(in_features=4, out_features=4, bias=True)
)
(tensor([[ 0.7272,  0.6301,  0.7847, -0.0701],
        [ 0.8097,  0.7174,  0.7150, -0.3013],
        [ 0.5427,  0.7218,  0.7113,  0.2315]], grad_fn=<TanhBackward>), tensor([[ 0.7272,  0.6301,  0.7847, -0.0701],
        [ 0.8097,  0.7174,  0.7150, -0.3013],
        [ 0.5427,  0.7218,  0.7113,  0.2315]], grad_fn=<TanhBackward>))
'''