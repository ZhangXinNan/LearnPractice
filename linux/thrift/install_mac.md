
参考官方安装文档：
```
./configure --prefix=/usr/local/ --with-boost=/usr/local --with-libevent=/usr/local
```

# 1 出现问题：Bison
## 错误信息
```
checking dynamic linker characteristics... darwin17.4.0 dyld
checking how to hardcode library paths into programs... immediate
checking whether make sets $(MAKE)... (cached) yes
checking for bison... yes
checking for bison version >= 2.5... no
configure: error: Bison version 2.5 or higher must be installed on the system!
```


## 解决办法
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


# 2  fatal error: 'openssl/opensslv.h' file not found
## 错误信息
```
➜  cpp git:(zxdev_mac) make
Making all in .
depbase=`echo src/thrift/transport/TSSLSocket.lo | sed 's|[^/]*$|.deps/&|;s|\.lo$||'`;\
	/bin/sh ../../libtool  --tag=CXX   --mode=compile /usr/bin/g++ -std=c++11 -DHAVE_CONFIG_H -I. -I../.. -I../../lib/cpp/src/thrift -I../../lib/c_glib/src/thrift  -I/usr/local/include  -I./src -D__STDC_FORMAT_MACROS -D__STDC_LIMIT_MACROS  -Wall -Wextra -pedantic -g -O2 -MT src/thrift/transport/TSSLSocket.lo -MD -MP -MF $depbase.Tpo -c -o src/thrift/transport/TSSLSocket.lo src/thrift/transport/TSSLSocket.cpp &&\
	mv -f $depbase.Tpo $depbase.Plo
libtool: compile:  /usr/bin/g++ -std=c++11 -DHAVE_CONFIG_H -I. -I../.. -I../../lib/cpp/src/thrift -I../../lib/c_glib/src/thrift -I/usr/local/include -I./src -D__STDC_FORMAT_MACROS -D__STDC_LIMIT_MACROS -Wall -Wextra -pedantic -g -O2 -MT src/thrift/transport/TSSLSocket.lo -MD -MP -MF src/thrift/transport/.deps/TSSLSocket.Tpo -c src/thrift/transport/TSSLSocket.cpp  -fno-common -DPIC -o src/thrift/transport/.libs/TSSLSocket.o
src/thrift/transport/TSSLSocket.cpp:43:10: fatal error: 'openssl/opensslv.h' file not found
#include <openssl/opensslv.h>
         ^~~~~~~~~~~~~~~~~~~~
1 error generated.
make[1]: *** [src/thrift/transport/TSSLSocket.lo] Error 1
make: *** [all-recursive] Error 1

```



## 解决办法：
```
./configure --prefix=/usr/local/ --with-boost=/usr/local --with-libevent=/usr/local LDFLAGS='-L/usr/local/opt/openssl/lib' CPPFLAGS='-I/usr/local/opt/openssl/include'

make
```

# 3 
## 错误信息
```
find blib -name 'Makefile*' -exec rm -f {} \;
Making all in php
Making all in test
composer install --working-dir=../../..
make[4]: composer: No such file or directory
make[4]: *** [deps] Error 1
make[3]: *** [all-recursive] Error 1
make[2]: *** [all-recursive] Error 1
make[1]: *** [all-recursive] Error 1
make: *** [all] Error 2
```

# 4
## 错误信息
```
/Users/zhangxin/tools/thrift-0.11.0/lib/php/src/ext/thrift_protocol/php_thrift_protocol.cpp:23:10: fatal error: 'php.h' file not found
#include "php.h"
         ^~~~~~~
1 error generated.
make[5]: *** [php_thrift_protocol.lo] Error 1
make[4]: *** [src/ext/thrift_protocol/modules/thrift_protocol.so] Error 2
make[3]: *** [all-recursive] Error 1
make[2]: *** [all-recursive] Error 1
make[1]: *** [all-recursive] Error 1
make: *** [all] Error 2

```

## 解决办法
```
./configure --prefix=/usr/local/ --with-boost=/usr/local --with-libevent=/usr/local LDFLAGS='-L/usr/local/opt/openssl/lib' CPPFLAGS='-I/usr/local/opt/openssl/include' --without-php --without-php_extension --without-go --without-js --without-perl --without-nodejs --without-lua

```