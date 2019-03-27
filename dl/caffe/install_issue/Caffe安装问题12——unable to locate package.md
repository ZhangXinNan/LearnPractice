

## 在Ubuntu 16.04上安装Caffe依赖软件时，出现问题：
```
E: Unable to locate package libprotobuf-dev
等等等
```


## 解决办法：
```
sudo apt update
sudo apt upgrade
```


## update和upgrade的区别：
[hat is the difference between apt-get update and upgrade?](https://askubuntu.com/questions/94102/what-is-the-difference-between-apt-get-update-and-upgrade)

You should first run update, then upgrade. Neither of them automatically runs the other.

* apt-get update updates the list of available packages and their versions, but it does not install or upgrade any packages.
* apt-get upgrade actually installs newer versions of the packages you have. After updating the lists, the package manager knows about available updates for the software you have installed. This is why you first want to update.


