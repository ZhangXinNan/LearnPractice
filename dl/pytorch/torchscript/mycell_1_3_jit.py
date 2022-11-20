
import torch


class MyDecisionGate(torch.nn.Module):
    def forward(self, x):
        if x.sum() > 0:
            return x
        else:
            return -x

class MyCell(torch.nn.Module):
    def __init__(self, dg):
        super(MyCell, self).__init__()
        self.dg = dg
        self.linear = torch.nn.Linear(4, 4)

    def forward(self, x, h):
        new_h = torch.tanh(self.dg(self.linear(x)) + h)
        return new_h, new_h

my_cell = MyCell(MyDecisionGate())
print(my_cell)
'''
MyCell(
  (dg): MyDecisionGate()
  (linear): Linear(in_features=4, out_features=4, bias=True)
)
'''
x = torch.rand(3, 4)
h = torch.rand(3, 4)
print(my_cell(x, h))
'''
(tensor([[ 0.5325,  0.8844,  0.0054, -0.0054],
        [ 0.5132,  0.7188,  0.2903,  0.2219],
        [ 0.8394,  0.5215,  0.5514,  0.5901]], grad_fn=<TanhBackward>), tensor([[ 0.5325,  0.8844,  0.0054, -0.0054],
        [ 0.5132,  0.7188,  0.2903,  0.2219],
        [ 0.8394,  0.5215,  0.5514,  0.5901]], grad_fn=<TanhBackward>))
'''

traced_cell = torch.jit.trace(my_cell, (x, h))
print(traced_cell.code)
'''
mycell_1_3_jit.py:7: TracerWarning: Converting a tensor to a Python boolean might cause the trace to be incorrect. We can't record the data flow of Python values, so this value will be treated as a constant in the future. This means that the trace might not generalize to other inputs!
  if x.sum() > 0:
def forward(self,
    input: Tensor,
    h: Tensor) -> Tuple[Tensor, Tensor]:
  _0 = (self.dg).forward((self.linear).forward(input, ), )
  _1 = torch.tanh(torch.add(_0, h, alpha=1))
  return (_1, _1)
'''