

import os
from io import BytesIO

content = open('read_txt.py', 'rb').read()
print(type(content), content)

s = content.decode()
print(type(s), s)