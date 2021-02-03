
from flask import Flask
app = Flask(__name__)
'''
@app.route('/')
def hello():
    return 'hello world ! '
'''
@app.route('/')
def sys_status():
	return 'server starts-up successful!'

if __name__ == '__main__':
	# app.run(port=5000)
    app.run()




