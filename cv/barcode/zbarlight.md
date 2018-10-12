## 安装zbar

```
on Debian, apt-get install libzbar0 libzbar-dev
on Mac OS X, brew install zbar
```

## 安装 zbarlight
```
pip install zbarlight
```

### 问题1 OSError: [Errno 13] Permission denied: '/Library/Python/2.7/site-packages/zbarlight'
```
➜  zbarlight git:(zxdev) ✗ pip install zbarlight
Collecting zbarlight
Requirement already satisfied: Pillow in /Users/zhangxin/Library/Python/2.7/lib/python/site-packages (from zbarlight)
Requirement already satisfied: olefile in /Users/zhangxin/Library/Python/2.7/lib/python/site-packages (from Pillow->zbarlight)
Installing collected packages: zbarlight
Exception:
Traceback (most recent call last):
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/basecommand.py", line 215, in main
    status = self.run(options, args)
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/commands/install.py", line 342, in run
    prefix=options.prefix_path,
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/req/req_set.py", line 784, in install
    **kwargs
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/req/req_install.py", line 851, in install
    self.move_wheel_files(self.source_dir, root=root, prefix=prefix)
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/req/req_install.py", line 1064, in move_wheel_files
    isolated=self.isolated,
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/wheel.py", line 345, in move_wheel_files
    clobber(source, lib_dir, True)
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/wheel.py", line 316, in clobber
    ensure_dir(destdir)
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/utils/__init__.py", line 83, in ensure_dir
    os.makedirs(path)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/os.py", line 157, in makedirs
    mkdir(name, mode)
OSError: [Errno 13] Permission denied: '/Library/Python/2.7/site-packages/zbarlight'
```

解决方法：
```
sudo chown -R $USER /Library/Python/2.7/site-packages/
```