
import torch 
from torchvision.models import resnet18 
 
# 使用PyTorch model zoo中的resnet18作为例子 
model = resnet18() 
model.eval() 
 
# 通过trace的方法生成IR需要一个输入样例 
dummy_input = torch.rand(1, 3, 224, 224) 
 
# IR生成 
with torch.no_grad(): 
    jit_model = torch.jit.trace(model, dummy_input) 

jit_layer1 = jit_model.layer1 
print(jit_layer1.graph) 
 
print(jit_layer1.code)


torch._C._jit_pass_inline(jit_layer1.graph) 
print(jit_layer1.code) 
