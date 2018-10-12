

Mac安装mysql-python
```
pip install mysql-python 
```
问题：
```
➜  shell pip install mysql-python 
Collecting mysql-python
  Using cached MySQL-python-1.2.5.zip
Building wheels for collected packages: mysql-python
  Running setup.py bdist_wheel for mysql-python ... error
  Complete output from command /Users/zhangxin/anaconda2/bin/python -u -c "import setuptools, tokenize;__file__='/private/var/folders/f_/shl432s55dl5766kw7tc5zsr0000gn/T/pip-build-D7BJgA/mysql-python/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" bdist_wheel -d /var/folders/f_/shl432s55dl5766kw7tc5zsr0000gn/T/tmpyu363ipip-wheel- --python-tag cp27:
  running bdist_wheel
  running build
  running build_py
  creating build
  creating build/lib.macosx-10.6-x86_64-2.7
  copying _mysql_exceptions.py -> build/lib.macosx-10.6-x86_64-2.7
  creating build/lib.macosx-10.6-x86_64-2.7/MySQLdb
  copying MySQLdb/__init__.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb
  copying MySQLdb/converters.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb
  copying MySQLdb/connections.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb
  copying MySQLdb/cursors.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb
  copying MySQLdb/release.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb
  copying MySQLdb/times.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb
  creating build/lib.macosx-10.6-x86_64-2.7/MySQLdb/constants
  copying MySQLdb/constants/__init__.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb/constants
  copying MySQLdb/constants/CR.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb/constants
  copying MySQLdb/constants/FIELD_TYPE.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb/constants
  copying MySQLdb/constants/ER.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb/constants
  copying MySQLdb/constants/FLAG.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb/constants
  copying MySQLdb/constants/REFRESH.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb/constants
  copying MySQLdb/constants/CLIENT.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb/constants
  running build_ext
  building '_mysql' extension
  creating build/temp.macosx-10.6-x86_64-2.7
  /usr/bin/gcc -fno-strict-aliasing -I/Users/zhangxin/anaconda2/include -arch x86_64 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes /usr/local/opt/openssl/lib -Dversion_info=(1,2,5,'final',1) -D__version__=1.2.5 -I/usr/local/Cellar/mysql/5.7.20/include/mysql -I/Users/zhangxin/anaconda2/include/python2.7 -c _mysql.c -o build/temp.macosx-10.6-x86_64-2.7/_mysql.o
  clang: warning: /usr/local/opt/openssl/lib: 'linker' input unused [-Wunused-command-line-argument]
  _mysql.c:1589:10: warning: comparison of unsigned expression < 0 is always false [-Wtautological-compare]
          if (how < 0 || how >= sizeof(row_converters)) {
              ~~~ ^ ~
  1 warning generated.
  /usr/bin/gcc -bundle -undefined dynamic_lookup -L/Users/zhangxin/anaconda2/lib -arch x86_64 /usr/local/opt/openssl/include /usr/local/opt/openssl/lib -arch x86_64 build/temp.macosx-10.6-x86_64-2.7/_mysql.o -L/usr/local/Cellar/mysql/5.7.20/lib -L/Users/zhangxin/anaconda2/lib -lmysqlclient -lssl -lcrypto -o build/lib.macosx-10.6-x86_64-2.7/_mysql.so
  ld: can't map file, errno=22 file '/usr/local/opt/openssl/include' for architecture x86_64
  clang: error: linker command failed with exit code 1 (use -v to see invocation)
  error: command '/usr/bin/gcc' failed with exit status 1
  
  ----------------------------------------
  Failed building wheel for mysql-python
  Running setup.py clean for mysql-python
Failed to build mysql-python
Installing collected packages: mysql-python
  Running setup.py install for mysql-python ... error
    Complete output from command /Users/zhangxin/anaconda2/bin/python -u -c "import setuptools, tokenize;__file__='/private/var/folders/f_/shl432s55dl5766kw7tc5zsr0000gn/T/pip-build-D7BJgA/mysql-python/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /var/folders/f_/shl432s55dl5766kw7tc5zsr0000gn/T/pip-DcCQhB-record/install-record.txt --single-version-externally-managed --compile:
    running install
    running build
    running build_py
    creating build
    creating build/lib.macosx-10.6-x86_64-2.7
    copying _mysql_exceptions.py -> build/lib.macosx-10.6-x86_64-2.7
    creating build/lib.macosx-10.6-x86_64-2.7/MySQLdb
    copying MySQLdb/__init__.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb
    copying MySQLdb/converters.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb
    copying MySQLdb/connections.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb
    copying MySQLdb/cursors.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb
    copying MySQLdb/release.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb
    copying MySQLdb/times.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb
    creating build/lib.macosx-10.6-x86_64-2.7/MySQLdb/constants
    copying MySQLdb/constants/__init__.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb/constants
    copying MySQLdb/constants/CR.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb/constants
    copying MySQLdb/constants/FIELD_TYPE.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb/constants
    copying MySQLdb/constants/ER.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb/constants
    copying MySQLdb/constants/FLAG.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb/constants
    copying MySQLdb/constants/REFRESH.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb/constants
    copying MySQLdb/constants/CLIENT.py -> build/lib.macosx-10.6-x86_64-2.7/MySQLdb/constants
    running build_ext
    building '_mysql' extension
    creating build/temp.macosx-10.6-x86_64-2.7
    /usr/bin/gcc -fno-strict-aliasing -I/Users/zhangxin/anaconda2/include -arch x86_64 -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes /usr/local/opt/openssl/lib -Dversion_info=(1,2,5,'final',1) -D__version__=1.2.5 -I/usr/local/Cellar/mysql/5.7.20/include/mysql -I/Users/zhangxin/anaconda2/include/python2.7 -c _mysql.c -o build/temp.macosx-10.6-x86_64-2.7/_mysql.o
    clang: warning: /usr/local/opt/openssl/lib: 'linker' input unused [-Wunused-command-line-argument]
    _mysql.c:1589:10: warning: comparison of unsigned expression < 0 is always false [-Wtautological-compare]
            if (how < 0 || how >= sizeof(row_converters)) {
                ~~~ ^ ~
    1 warning generated.
    /usr/bin/gcc -bundle -undefined dynamic_lookup -L/Users/zhangxin/anaconda2/lib -arch x86_64 /usr/local/opt/openssl/include /usr/local/opt/openssl/lib -arch x86_64 build/temp.macosx-10.6-x86_64-2.7/_mysql.o -L/usr/local/Cellar/mysql/5.7.20/lib -L/Users/zhangxin/anaconda2/lib -lmysqlclient -lssl -lcrypto -o build/lib.macosx-10.6-x86_64-2.7/_mysql.so
    ld: can't map file, errno=22 file '/usr/local/opt/openssl/lib' for architecture x86_64
    clang: error: linker command failed with exit code 1 (use -v to see invocation)
    error: command '/usr/bin/gcc' failed with exit status 1
    
    ----------------------------------------
Command "/Users/zhangxin/anaconda2/bin/python -u -c "import setuptools, tokenize;__file__='/private/var/folders/f_/shl432s55dl5766kw7tc5zsr0000gn/T/pip-build-D7BJgA/mysql-python/setup.py';f=getattr(tokenize, 'open', open)(__file__);code=f.read().replace('\r\n', '\n');f.close();exec(compile(code, __file__, 'exec'))" install --record /var/folders/f_/shl432s55dl5766kw7tc5zsr0000gn/T/pip-DcCQhB-record/install-record.txt --single-version-externally-managed --compile" failed with error code 1 in /private/var/folders/f_/shl432s55dl5766kw7tc5zsr0000gn/T/pip-build-D7BJgA/mysql-python/
```



尝试办法1：
```
brew install caskroom/cask/mysql-connector-python
# 并不能解决 import MySQLdb
ImportError: No module named MySQLdb
的问题
```
深度方法2：
```
➜  mysql_db git:(zxdev_mac) ✗ easy_install mysql-python
Searching for mysql-python
Reading https://pypi.python.org/simple/mysql-python/
Downloading https://pypi.python.org/packages/a5/e9/51b544da85a36a68debe7a7091f068d802fc515a3a202652828c73453cad/MySQL-python-1.2.5.zip#md5=654f75b302db6ed8dc5a898c625e030c
Best match: MySQL-python 1.2.5
Processing MySQL-python-1.2.5.zip
Writing /var/folders/f_/shl432s55dl5766kw7tc5zsr0000gn/T/easy_install-vU9URE/MySQL-python-1.2.5/setup.cfg
Running MySQL-python-1.2.5/setup.py -q bdist_egg --dist-dir /var/folders/f_/shl432s55dl5766kw7tc5zsr0000gn/T/easy_install-vU9URE/MySQL-python-1.2.5/egg-dist-tmp-A53OJf
clang: warning: /usr/local/opt/openssl/lib: 'linker' input unused [-Wunused-command-line-argument]
_mysql.c:1589:10: warning: comparison of unsigned expression < 0 is always false [-Wtautological-compare]
        if (how < 0 || how >= sizeof(row_converters)) {
            ~~~ ^ ~
1 warning generated.
ld: can't map file, errno=22 file '/usr/local/opt/openssl/include' for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
error: Setup script exited with error: command '/usr/bin/gcc' failed with exit status 1
```


尝试方法3:
```
pip install pymysql 
```


尝试方法4：
```
import pymysql
pymysql.install_as_MySQLdb()
```