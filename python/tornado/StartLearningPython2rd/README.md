[《零基础学Python》第二版   为做网站而准备](http://wiki.jikexueyuan.com/project/start-learning-python/301.html)

# 安装mysql
## mac下安装mysql
```
brew install mysql
```

## 启动
```
brew services start mysql
# or
mysql.server start
# ubuntu 
service mysqld start
```

## 设置密码，简单起见，我没有设
```
GRANT ALL PRIVILEGES ON *.* TO root@localhost IDENTIFIED BY "123456";
```

## 连接到数据库
```
mysql -u root -p
```

## 建立一个数据库/表，插入数据
```mysql
create database qiwsirtest character set utf8;
use qiwsirtest;
show tables;

create table users(id int(2) not null primary key auto_increment,username varchar(40),password text,email text)default charset=utf8;

insert into users(username,password,email) values("qiwsir","123123","qiwsir@gmail.com");
```

# 安装 Python-MySQLdb
Python-MySQLdb 是一个接口程序，Python 通过它对 mysql 数据实现各种操作。

```
pip install mysql-Python
```

在python下执行：
```
import MySQLdb
conn = MySQLdb.connect(host="localhost",user="root",passwd="",db="qiwsirtest",port=3306,charset="utf8")

cur = conn.cursor()
cur.execute("insert into users (username,password,email) values (%s,%s,%s)",("Python","123456","Python@gmail.com"))
conn.commit()
```

