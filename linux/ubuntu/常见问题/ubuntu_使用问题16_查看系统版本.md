


# 1 ubuntu 版本号
```bash
cat /etc/issue
```
输出
```
Ubuntu 18.04.5 LTS \n \l
```

或者
```bash
lsb_release -a
```
输出
```
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 18.04.5 LTS
Release:        18.04
Codename:       bionic
```

# 2 查看系统内核版本
```bash
cat /proc/version
```
输出
```
Linux version 5.4.0-80-generic (buildd@lcy01-amd64-028) (gcc version 7.5.0 (Ubuntu 7.5.0-3ubuntu1~18.04)) #90~18.04.1-Ubuntu SMP Tue Jul 13 19:40:02 UTC 2021
```

或者
```bash
uname -a
```
输出：
```
Linux dell-Precision-7920-Tower 5.4.0-80-generic #90~18.04.1-Ubuntu SMP Tue Jul 13 19:40:02 UTC 2021 x86_64 x86_64 x86_64 GNU/Linux
```

