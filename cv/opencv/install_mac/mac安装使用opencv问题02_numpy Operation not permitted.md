
## 问题2：pip install numpy --upgrade
```
➜  feature git:(master) ✗ pip install numpy --upgrade
Collecting numpy
  Using cached numpy-1.13.3-cp27-cp27m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl
Installing collected packages: numpy
  Found existing installation: numpy 1.8.0rc1
    DEPRECATION: Uninstalling a distutils installed project (numpy) has been deprecated and will be removed in a future version. This is due to the fact that uninstalling a distutils project will only partially uninstall the project.
    Uninstalling numpy-1.8.0rc1:
Exception:
Traceback (most recent call last):
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/basecommand.py", line 215, in main
    status = self.run(options, args)
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/commands/install.py", line 342, in run
    prefix=options.prefix_path,
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/req/req_set.py", line 778, in install
    requirement.uninstall(auto_confirm=True)
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/req/req_install.py", line 754, in uninstall
    paths_to_remove.remove(auto_confirm)
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/req/req_uninstall.py", line 115, in remove
    renames(path, new_path)
  File "/Library/Python/2.7/site-packages/pip-9.0.1-py2.7.egg/pip/utils/__init__.py", line 267, in renames
    shutil.move(old, new)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/shutil.py", line 302, in move
    copy2(src, real_dst)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/shutil.py", line 131, in copy2
    copystat(src, dst)
  File "/System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/shutil.py", line 103, in copystat
    os.chflags(dst, st.st_flags)
OSError: [Errno 1] Operation not permitted: '/var/folders/f_/shl432s55dl5766kw7tc5zsr0000gn/T/pip-RlvgIz-uninstall/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/numpy-1.8.0rc1-py2.7.egg-info'
```

查看numpy的path
```
➜  feature git:(master) ✗ python -c 'import numpy as np; print np.__path__'
['/System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python/numpy']
```

```
➜  feature git:(master) ✗ brew link numpy
Linking /usr/local/Cellar/numpy/1.13.3... 
Error: Could not symlink lib/python2.7/site-packages/numpy/__config__.py
Target /usr/local/lib/python2.7/site-packages/numpy/__config__.py
already exists. You may want to remove it:
  rm '/usr/local/lib/python2.7/site-packages/numpy/__config__.py'

To force the link and overwrite all conflicting files:
  brew link --overwrite numpy

To list all files that would be deleted:
  brew link --overwrite --dry-run numpy
```