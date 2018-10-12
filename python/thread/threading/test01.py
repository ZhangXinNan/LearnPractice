#encoding=utf8

import threading, time

count = 0
class MyThread(threading.Thread):
    def __init__(self, threadName):
        super(MyThread, self).__init__(name=threadName)
    
    def run(self):
        global count
        for i in range(10):
            count = count + 1
            time.sleep(0.3)
            print(self.getName(), count)


for i in range(3):
    MyThread('MyThreadName:'+str(i)).start()