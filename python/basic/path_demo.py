
import os

__dir__ = os.path.dirname(__file__)
print(__dir__)

__dir__ = os.path.dirname(os.path.abspath(__file__))
print(__dir__)

import pathlib
__dir__ = pathlib.Path(__file__).absolute().parent
print(__dir__)
print(str(__dir__), type(__dir__))

dir_name = os.path.dirname(os.path.abspath(__file__))
print(dir_name)

print(os.path.abspath(os.path.join(dir_name, '../../')))


from pathlib import Path
# 当前文件的绝对路径
__dir__ = Path(__file__).resolve()
print(type(__dir__), __dir__)
str_dir = str(__dir__)
print(type(str_dir), str_dir)



