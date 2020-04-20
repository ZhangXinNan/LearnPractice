# coding=utf-8
from flask import Flask
from flask import request
# 所有 Flask 程序都必须创建一个程序实例
# Web服务器使用WSGI协议,把接收客户端的所有请求转交给这个对象处理
app = Flask(__name__)


# 客户端--(请求)-->Web 服务器 --(请求)-->Flask程序实例--(URL)-->路由;路由
# 程序实例需要知道每个 URL 请求运行哪些代码,所以保存了一个 URL 到 Python 函数的映射关系
# 处理 URL 与函数映射关系的程序是路由
# 视图函数 (view funtion) 
@app.route('/')
def hello_world():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' % user_agent, 400
    #return '<h1>Hello World!<h1>'

# <>中的是动态部分
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello , %s ! </h1>' % name

if __name__ == '__main__':
    # 程序实例用 run 方法启动 Flask 集成的开发Web 服务器
    app.run(host='0.0.0.0', port=9000)

