
# 1 问题

```bash
(py36_pytorch101) C:\Users\zhang>pip install lanms
Collecting lanms
  Downloading https://files.pythonhosted.org/packages/96/c0/50dc2c857ed060e907adaef31184413a7706e475c322236d346382e45195/lanms-1.0.2.tar.gz (973kB)
     |████████████████████████████████| 983kB 11kB/s
    ERROR: Command errored out with exit status 1:
     command: 'D:\ProgramData\Anaconda3\envs\py36_pytorch101\python.exe' -c 'import sys, setuptools, tokenize; sys.argv[0] = '"'"'C:\\Users\\zhang\\AppData\\Local\\Temp\\pip-install-qg7zgh3b\\lanms\\setup.py'"'"'; __file__='"'"'C:\\Users\\zhang\\AppData\\Local\\Temp\\pip-install-qg7zgh3b\\lanms\\setup.py'"'"';f=getattr(tokenize, '"'"'open'"'"', open)(__file__);code=f.read().replace('"'"'\r\n'"'"', '"'"'\n'"'"');f.close();exec(compile(code, __file__, '"'"'exec'"'"'))' egg_info --egg-base 'C:\Users\zhang\AppData\Local\Temp\pip-install-qg7zgh3b\lanms\pip-egg-info'
         cwd: C:\Users\zhang\AppData\Local\Temp\pip-install-qg7zgh3b\lanms\
    Complete output (11 lines):
    Traceback (most recent call last):
      File "<string>", line 1, in <module>
      File "C:\Users\zhang\AppData\Local\Temp\pip-install-qg7zgh3b\lanms\setup.py", line 27, in <module>
        if subprocess.call(['make', '--always-make','-C', BASE_DIR]) != 0:
      File "D:\ProgramData\Anaconda3\envs\py36_pytorch101\lib\subprocess.py", line 287, in call
        with Popen(*popenargs, **kwargs) as p:
      File "D:\ProgramData\Anaconda3\envs\py36_pytorch101\lib\subprocess.py", line 729, in __init__
        restore_signals, start_new_session)
      File "D:\ProgramData\Anaconda3\envs\py36_pytorch101\lib\subprocess.py", line 1017, in _execute_child
        startupinfo)
    FileNotFoundError: [WinError 2] 系统找不到指定的文件。
    ----------------------------------------
ERROR: Command errored out with exit status 1: python setup.py egg_info Check the logs for full command output.
```


```bash
(py37_pytorch101) ➜  EAST-SakuraRiven git:(zxdev) ✗ python detect_zx.py 
find: -xtype: unknown primary or operator
make: `adaptor.so' is up to date.
pytorch version : 1.0.1.post2
[1]    8238 segmentation fault  python detect_zx.py
```
注释掉lanms部分，则能运行并出结果 。


# 2 解决
## 2.1 升级pip setuptools，没有解决
```bash
pip install—upgrade pip
pip install --upgrade setuptools
```


## 2.2 参考pybind11的方法，添加segup.py进行编译
