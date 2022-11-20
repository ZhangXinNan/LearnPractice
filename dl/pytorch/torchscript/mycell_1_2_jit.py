
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
traced_cell = torch.jit.trace(my_cell, (x, h))
print(traced_cell)
traced_cell(x, h)
'''
MyCell(
  (linear): Linear(in_features=4, out_features=4, bias=True)
)
MyCell(
  original_name=MyCell
  (linear): Linear(original_name=Linear)
)
'''


print(traced_cell.graph)
'''
graph(%self.1 : __torch__.MyCell,
      %input : Float(3, 4, strides=[4, 1], requires_grad=0, device=cpu),
      %h : Float(3, 4, strides=[4, 1], requires_grad=0, device=cpu)):
  %21 : __torch__.torch.nn.modules.linear.Linear = prim::GetAttr[name="linear"](%self.1)
  %23 : Tensor = prim::CallMethod[name="forward"](%21, %input)
  %14 : int = prim::Constant[value=1]() # mycell_2_1.py:11:0
  %15 : Float(3, 4, strides=[4, 1], requires_grad=1, device=cpu) = aten::add(%23, %h, %14) # mycell_2_1.py:11:0
  %16 : Float(3, 4, strides=[4, 1], requires_grad=1, device=cpu) = aten::tanh(%15) # mycell_2_1.py:11:0
  %17 : (Float(3, 4, strides=[4, 1], requires_grad=1, device=cpu), Float(3, 4, strides=[4, 1], requires_grad=1, device=cpu)) = prim::TupleConstruct(%16, %16)
  return (%17)
'''

print(traced_cell.code)

'''
def forward(self,
    input: Tensor,
    h: Tensor) -> Tuple[Tensor, Tensor]:
  _0 = torch.add((self.linear).forward(input, ), h, alpha=1)
  _1 = torch.tanh(_0)
  return (_1, _1)
'''

