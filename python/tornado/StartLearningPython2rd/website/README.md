

# 一个基本框架
```
/.
|
handlers
|
methods
|
statics
|
templates
|
application.py
|
server.py
|
url.py
```

# 依次说明上面的架势中每个目录和文件的作用
* handlers：我准备在这个文件夹中放前面所说的后端 Python 程序，主要处理来自前端的请求，并且操作数据库。
* methods：这里准备放一些函数或者类，比如用的最多的读写数据库的函数，这些函数被 handlers 里面的程序使用。
* statics：这里准备放一些静态文件，比如图片，css 和 javascript 文件等。
* templates：这里放模板文件，都是以 html 为扩展名的，它们将直接面对用户。




