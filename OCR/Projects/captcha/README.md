```
➜  captcha git:(master) ✗ python
Python 2.7.13 (default, Apr  4 2017, 08:46:44) 
[GCC 4.2.1 Compatible Apple LLVM 8.0.0 (clang-800.0.42.1)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import captcha
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "captcha.py", line 2, in <module>
    from captcha.image import ImageCaptcha
ImportError: No module named image
```

解决方法：目录下有以captcha的python脚本文件。