[pkg-config的一些用法](https://blog.csdn.net/luotuo44/article/details/24836901)
[使用pkg-config工具](https://my.oschina.net/shelllife/blog/1533653)


# 用处
pkg-config能够把这些头文件和库文件的位置指出来，给编译器使用。
```
`pkg-config --cflags --libs gtk+-2.0`
```
* --cflags 给出编译时需要的选项
* --libs 给出链接时的选项

# 配置
pkg-config命令是通过查询XXX.pc文件而知道第三方库的头文件和库文件所在的位置。


pkg-config又是如何找到所需的.pc文件呢？这就需要用到一个环境变量PKG_CONFIG_PATH了。
/usr/local/lib/pkgconfig
```
PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig
# /usr/local/lib/pkgconfig 或者 /usr/lib/pkgconfig
export PKG_CONFIG_PATH
```

为了使库的设置变得简单一些，可以把下面的这两句设置保存到一个文件中（比如 set_gtk-2.10 文件）:
```
export PKG_CONFIG_PATH=/opt/gtk/lib/pkgconfig:$PKG_CONFIG_PATH
export LD_LIBRARY_PATH=/opt/gtk/lib:$LD_LIBRARY_PATH
```

# 库文件的搜索
库文件在连接（静态库和共享库）和运行（仅限于使用共享库的程序）时被使用，其搜索路径是在系统中进行设置的。一般 Linux 系统把 /lib 和 /usr/lib 两个目录作为默认的库搜索路径，所以使用这两个目录中的库时不需要进行设置搜索路径即可直接使用。对于处于默认库搜索路径之外的库，需要将库的位置添加到库的搜索路径之中。设置库文件的搜索路径有下列两种方式，可任选其一使用：

- 在环境变量 LD_LIBRARY_PATH 中指明库的搜索路径。
- 在 /etc/ld.so.conf 文件中添加库的搜索路径。


第二种搜索路径的设置方式对于程序连接时的库（包括共享库和静态库）的定位已经足够了，但是对于使用了共享库的程序的执行还是不够的。因为为了加快程序执行时对共享库的定位速度，避免使用搜索路径查找共享库的低效率，所以是直接读取库列表文件 /etc/ld.so.cache 从中进行搜索的。/etc/ld.so.cache 是一个非文本的数据文件，不能直接编辑，它是根据 /etc/ld.so.conf 中设置的搜索路径由 /sbin/ldconfig 命令将这些搜索路径下的共享库文件集中在一起而生成的（ldconfig 命令要以 root 权限执行）。因此为了保证程序执行时对库的定位，在 /etc/ld.so.conf 中进行了库搜索路径的设置之后，还必须要运行 /sbin/ldconfig 命令更新 /etc/ld.so.cache 文件之后才可以。

**ldconfig**，它的作用就是**将 /etc/ld.so.conf 列出的路径下的库文件缓存到/etc/ld.so.cache以供使用**。因此当安装完一些库文件（例如刚安装好 glib 或者修改 ld.so.conf 增加新的库路径)后，需要运行一下 /sbin/ldconfig 使所有的库文件都被缓存到 ld.so.cache 中，如果没做，即使库文件明明就在 /usr/lib下的，也是不会被使用的。

在程序连接时，对于库文件（静态库和共享库）的搜索路径，除了上面的设置方式之外，还可以通过 -L 参数显式指定。因为用 -L 设置的路径将被优先搜索，所以在连接的时候通常都会以这种方式直接指定要连接的库的路径
