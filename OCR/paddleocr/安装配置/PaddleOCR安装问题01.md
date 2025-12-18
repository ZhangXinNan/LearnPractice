
# 1. 问题描述

ERROR: Could not build wheels for lxml, which is required to install pyproject.toml-based projects

# 2. 解决办法
The lxml package seems to cause such errors when Xcode Command Line Tools are not correctly installed or some paths are missing/broken. As implied in your terminal, first try:
```bash
$ xcode-select --install
```
The command above will install the required packages if not installed already. If you receive the error xcode-select: error: command line tools are already installed, use "Software Update" to install updates, try resetting Xcode Command Line Tools as follows. It will reset the path to the Xcode Command Line Tools directory, which may help with the issue.
```bash
$ sudo xcode-select --reset
```
After you install/update Xcode Command Line Tools, try installing lxml separately to see if your issue is resolved.
```bash
pip install lxml
```

# 3. 参考资料
https://stackoverflow.com/questions/76418822/error-could-not-build-wheels-for-lxml-which-is-required-to-install-pyproject-t

