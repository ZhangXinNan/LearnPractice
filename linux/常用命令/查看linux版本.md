[查看 Linux 发行版名称和版本号的 8 种方法](https://linux.cn/article-9586-1.html)
______


方法 1： lsb_release 命令
LSB（Linux 标准库Linux Standard Base）能够打印发行版的具体信息，包括发行版名称、版本号、代号等。

# lsb_release -a
No LSB modules are available.
Distributor ID: Ubuntu
Description: Ubuntu 16.04.3 LTS
Release: 16.04
Codename: xenial
方法 2： /etc/*-release 文件
release 文件通常被视为操作系统的标识。在 /etc 目录下放置了很多记录着发行版各种信息的文件，每个发行版都各自有一套这样记录着相关信息的文件。下面是一组在 Ubuntu/Debian 系统上显示出来的文件内容。

# cat /etc/issue
Ubuntu 16.04.3 LTS \n \l
# cat /etc/issue.net
Ubuntu 16.04.3 LTS
# cat /etc/lsb-release
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=16.04
DISTRIB_CODENAME=xenial
DISTRIB_DESCRIPTION="Ubuntu 16.04.3 LTS"
# cat /etc/os-release
NAME="Ubuntu"
VERSION="16.04.3 LTS (Xenial Xerus)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 16.04.3 LTS"
VERSION_ID="16.04"
HOME_URL="http://www.ubuntu.com/"
SUPPORT_URL="http://help.ubuntu.com/"
BUG_REPORT_URL="http://bugs.launchpad.net/ubuntu/"
VERSION_CODENAME=xenial
UBUNTU_CODENAME=xenial
# cat /etc/debian_version
9.3
下面这一组是在 RHEL/CentOS/Fedora 系统上显示出来的文件内容。其中 /etc/redhat-release 和 /etc/system-release 文件是指向 /etc/[发行版名称]-release 文件的一个连接。

# cat /etc/centos-release
CentOS release 6.9 (Final)
# cat /etc/fedora-release
Fedora release 27 (Twenty Seven)
# cat /etc/os-release
NAME=Fedora
VERSION="27 (Twenty Seven)"
ID=fedora
VERSION_ID=27
PRETTY_NAME="Fedora 27 (Twenty Seven)"
ANSI_COLOR="0;34"
CPE_NAME="cpe:/o:fedoraproject:fedora:27"
HOME_URL="https://fedoraproject.org/"
SUPPORT_URL="https://fedoraproject.org/wiki/Communicating_and_getting_help"
BUG_REPORT_URL="https://bugzilla.redhat.com/"
REDHAT_BUGZILLA_PRODUCT="Fedora"
REDHAT_BUGZILLA_PRODUCT_VERSION=27
REDHAT_SUPPORT_PRODUCT="Fedora"
REDHAT_SUPPORT_PRODUCT_VERSION=27
PRIVACY_POLICY_URL="https://fedoraproject.org/wiki/Legal:PrivacyPolicy"
# cat /etc/redhat-release
Fedora release 27 (Twenty Seven)
# cat /etc/system-release
Fedora release 27 (Twenty Seven)
方法 3： uname 命令
uname（unix name 的意思） 是一个打印系统信息的工具，包括内核名称、版本号、系统详细信息以及所运行的操作系统等等。

建议阅读： 6种查看系统 Linux 内核的方法
# uname -a
Linux localhost.localdomain 4.12.14-300.fc26.x86_64 #1 SMP Wed Sep 20 16:28:07 UTC 2017 x86_64 x86_64 x86_64 GNU/Linux
以上运行结果说明使用的操作系统版本是 Fedora 26。

方法 4： /proc/version 文件
这个文件记录了 Linux 内核的版本、用于编译内核的 gcc 的版本、内核编译的时间，以及内核编译者的用户名。

# cat /proc/version
Linux version 4.12.14-300.fc26.x86_64 ([email protected]) (gcc version 7.2.1 20170915 (Red Hat 7.2.1-2) (GCC) ) #1 SMP Wed Sep 20 16:28:07 UTC 2017
方法 5： dmesg 命令
dmesg（展示信息display message 或驱动程序信息driver message）是大多数类 Unix 操作系统上的一个命令，用于打印内核的消息缓冲区的信息。

# dmesg | grep "Linux"
[ 0.000000] Linux version 4.12.14-300.fc26.x86_64 ([email protected]) (gcc version 7.2.1 20170915 (Red Hat 7.2.1-2) (GCC) ) #1 SMP Wed Sep 20 16:28:07 UTC 2017
[ 0.001000] SELinux: Initializing.
[ 0.001000] SELinux: Starting in permissive mode
[ 0.470288] SELinux: Registering netfilter hooks
[ 0.616351] Linux agpgart interface v0.103
[ 0.630063] usb usb1: Manufacturer: Linux 4.12.14-300.fc26.x86_64 ehci_hcd
[ 0.688949] usb usb2: Manufacturer: Linux 4.12.14-300.fc26.x86_64 ohci_hcd
[ 2.564554] SELinux: Disabled at runtime.
[ 2.564584] SELinux: Unregistering netfilter hooks
方法 6： Yum/Dnf 命令
Yum（Yellowdog 更新器修改版Yellowdog Updater Modified）是 Linux 操作系统上的一个包管理工具，而 yum 命令被用于一些基于 RedHat 的 Linux 发行版上安装、更新、查找、删除软件包。

建议阅读： 在 RHEL/CentOS 系统上使用 yum 命令管理软件包
# yum info nano
Loaded plugins: fastestmirror, ovl
Loading mirror speeds from cached hostfile
 * base: centos.zswap.net
 * extras: mirror2.evolution-host.com
 * updates: centos.zswap.net
Available Packages
Name : nano
Arch : x86_64
Version : 2.3.1
Release : 10.el7
Size : 440 k
Repo : base/7/x86_64
Summary : A small text editor
URL : http://www.nano-editor.org
License : GPLv3+
Description : GNU nano is a small and friendly text editor.
下面的 yum repolist 命令执行后显示了 yum 的基础源仓库、额外源仓库、更新源仓库都来自 CentOS 7 仓库。

# yum repolist
Loaded plugins: fastestmirror, ovl
Loading mirror speeds from cached hostfile
 * base: centos.zswap.net
 * extras: mirror2.evolution-host.com
 * updates: centos.zswap.net
repo id repo name status
base/7/x86_64 CentOS-7 - Base 9591
extras/7/x86_64 CentOS-7 - Extras 388
updates/7/x86_64 CentOS-7 - Updates 1929
repolist: 11908
使用 dnf 命令也同样可以查看发行版名称和版本号。

建议阅读： 在 Fedora 系统上使用 DNF（YUM 的一个分支）命令管理软件包
# dnf info nano
Last metadata expiration check: 0:01:25 ago on Thu Feb 15 01:59:31 2018.
Installed Packages
Name : nano
Version : 2.8.7
Release : 1.fc27
Arch : x86_64
Size : 2.1 M
Source : nano-2.8.7-1.fc27.src.rpm
Repo : @System
From repo : fedora
Summary : A small text editor
URL : https://www.nano-editor.org
License : GPLv3+
Description : GNU nano is a small and friendly text editor.
方法 7： RPM 命令
RPM（红帽包管理器RedHat Package Manager）是在 CentOS、Oracle Linux、Fedora 这些基于 RedHat 的操作系统上的一个强大的命令行包管理工具，同样也可以帮助我们查看系统的版本信息。

建议阅读： 在基于 RHEL 的系统上使用 RPM 命令管理软件包
# rpm -q nano
nano-2.8.7-1.fc27.x86_64
方法 8： APT-GET 命令
Apt-Get（高级打包工具Advanced Packaging Tool）是一个强大的命令行工具，可以自动下载安装新软件包、更新已有的软件包、更新软件包列表索引，甚至更新整个 Debian 系统。

建议阅读： 在基于 Debian 的系统上使用 Apt-Get 和 Apt-Cache 命令管理软件包
# apt-cache policy nano
nano:
 Installed: 2.5.3-2ubuntu2
 Candidate: 2.5.3-2ubuntu2
 Version table:
 * 2.5.3-2ubuntu2 500
 500 http://nova.clouds.archive.ubuntu.com/ubuntu xenial-updates/main amd64 Packages
 100 /var/lib/dpkg/status
 2.5.3-2 500
 500 http://nova.clouds.archive.ubuntu.com/ubuntu xenial/main amd64 Packages