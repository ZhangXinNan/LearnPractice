
参考官方安装文档：
```
./configure --prefix=/usr/local/ --with-boost=/usr/local --with-libevent=/usr/local
```

出现问题：
```
checking dynamic linker characteristics... darwin17.4.0 dyld
checking how to hardcode library paths into programs... immediate
checking whether make sets $(MAKE)... (cached) yes
checking for bison... yes
checking for bison version >= 2.5... no
configure: error: Bison version 2.5 or higher must be installed on the system!
```


解决办法：
```
➜  thrift git:(zxdev_mac) brew upgrade bison
Updating Homebrew...
==> Upgrading 1 outdated package, with result:
bison 3.0.4_1
==> Upgrading bison 
==> Downloading https://homebrew.bintray.com/bottles/bison-3.0.4_1.high_sierra.bottle.tar.gz
######################################################################## 100.0%
==> Pouring bison-3.0.4_1.high_sierra.bottle.tar.gz
==> Caveats
This formula is keg-only, which means it was not symlinked into /usr/local,
because some formulae require a newer version of bison.

If you need to have this software first in your PATH run:
  echo 'export PATH="/usr/local/opt/bison/bin:$PATH"' >> ~/.zshrc

For compilers to find this software you may need to set:
    LDFLAGS:  -L/usr/local/opt/bison/lib

==> Summary
🍺  /usr/local/Cellar/bison/3.0.4_1: 52 files, 2MB
```