使用brew 在mac上安装了多个版本numpy，现在卸载不了。
```
➜  keras git:(zxdev_mac) brew uninstall numpy
Error: numpy has multiple installed versions
Use `brew uninstall --force numpy` to remove all versions.
➜  keras git:(zxdev_mac) brew uninstall --force numpy
Error: Refusing to uninstall /usr/local/Cellar/numpy/1.12.1
because it is required by matplotlib, which is currently installed.
You can override this and force removal with:
  brew uninstall --ignore-dependencies numpy
➜  keras git:(zxdev_mac) brew uninstall --ignore-dependencies numpy
Error: numpy has multiple installed versions
Use `brew uninstall --force numpy` to remove all versions.
```

解决方法：
```
brew uninstall --force --ignore-dependencies numpy
```