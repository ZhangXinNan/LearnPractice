

在安装软件时出现如下错误：
```bash
zhangxin@zhangxin-Alienware-17-R5:~$ sudo apt install zstd
[sudo] password for zhangxin: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
You might want to run 'apt-get -f install' to correct these:
The following packages have unmet dependencies:
 apt-utils : Depends: apt (= 1.2.27) but 1.2.29ubuntu0.1 is to be installed
 zstd : Depends: libzstd1 (= 1.3.1+dfsg-1~ubuntu0.16.04.1) but it is not going to be installed
E: Unmet dependencies. Try 'apt-get -f install' with no packages (or specify a solution).



zhangxin@zhangxin-Alienware-17-R5:~$ sudo apt-get -f install zstd
Reading package lists... Done
Building dependency tree       
Reading state information... Done
You might want to run 'apt-get -f install' to correct these:
The following packages have unmet dependencies:
 apt-utils : Depends: apt (= 1.2.27) but 1.2.29ubuntu0.1 is to be installed
 zstd : Depends: libzstd1 (= 1.3.1+dfsg-1~ubuntu0.16.04.1) but it is not going to be installed
E: Unmet dependencies. Try 'apt-get -f install' with no packages (or specify a solution).

```


安装tree工具时
```bash
zhangxin@zhangxin-Alienware-17-R5:~$ sudo apt-get install tree
Reading package lists... Done
Building dependency tree       
Reading state information... Done
You might want to run 'apt-get -f install' to correct these:
The following packages have unmet dependencies:
 apt-utils : Depends: apt (= 1.2.27) but 1.2.29ubuntu0.1 is to be installed
E: Unmet dependencies. Try 'apt-get -f install' with no packages (or specify a solution).
zhangxin@zhangxin-Alienware-17-R5:~$ sudo apt-get -f install tree
Reading package lists... Done
Building dependency tree       
Reading state information... Done
You might want to run 'apt-get -f install' to correct these:
The following packages have unmet dependencies:
 apt-utils : Depends: apt (= 1.2.27) but 1.2.29ubuntu0.1 is to be installed
E: Unmet dependencies. Try 'apt-get -f install' with no packages (or specify a solution).
```



解决方法：
```bash
sudo apt-get -f upgrade
```