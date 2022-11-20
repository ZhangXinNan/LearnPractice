import torch
import torch.nn as nn

m = nn.Linear(20, 30)
print(m)

input = torch.randn(128, 20)
print(input.size())
print(input)

output = m(input)
print(output.size())
print(output)
