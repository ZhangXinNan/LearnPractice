
from tkinter import E
import traceback

try:
    a = 3
except Exception as e:
    traceback.print_exc()


print(a)