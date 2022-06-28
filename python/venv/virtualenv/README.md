
创建一个独立的Python环境
```
virtualenv --no-site-packages venv
# --no-site-packages : 已经安装到系统Python环境中的所有第三方包都不会复制过来
# --python 或者 -p ： 指定python版本
```

进入该环境
```
source venv/bin/activate
```

退出当前环境
```
deactivate
```

