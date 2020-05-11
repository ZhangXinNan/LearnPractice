

# 1 问题
```
本地计算机上的mysql80 服务启动后停止 某些服务在未由其他服务或程序使用时将自动停止。
```

# 2 解决办法1

1. 删除data目录。
2. 使用管理员打开cmd。找到mysql的安装目录。切换到bin目录下。
3. 设置环境变量，可以使得在任意路径下，执行mysql等可执行程序。
4. 初始化data文件夹。
```bash
mysqld --initialize-insecure --user=mysql
```
4. 
```bash
# mysql服务没有安装。
mysqld.exe -install
# net start MySQL80
net start mysql
```

# 3 解决方法2

1. 设置环境变量，添加mysql的bin目录全路径到环境变量中。这样就可以使得在任意路径下，执行mysql等可执行程序。
2. 使用管理员身份证打开cmd，启动mysql服务。
```bash
net start mysql
```
