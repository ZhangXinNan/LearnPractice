
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