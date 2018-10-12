#encoding=utf8
'''
Lock类是threading中用于锁定当前线程的锁定类。
对当前运行中的线程进行锁定，只有当前线程被释放后，后续线程才可以继续操作。
'''
import threading, time, random



count = 0
class MyThread(threading.Thread):
    def __init__(self, lock, threadName):
        super(MyThread, self).__init__(name=threadName)
        self.lock = lock
    
    def run(self):
        global count
        self.lock.acquire()
        for i in range(10):
            count = count + 1
            time.sleep(0.3)
            print(self.getName(), count)
        self.lock.release()

lock = threading.Lock()
for i in range(3):
    MyThread(lock, 'MyThreadName:'+str(i)).start()

'''
➜  threading git:(master) ✗ python test02_lock.py 
('MyThreadName:0', 1)
('MyThreadName:0', 2)
('MyThreadName:0', 3)
('MyThreadName:0', 4)
('MyThreadName:0', 5)
('MyThreadName:0', 6)
('MyThreadName:0', 7)
('MyThreadName:0', 8)
('MyThreadName:0', 9)
('MyThreadName:0', 10)
('MyThreadName:1', 11)
('MyThreadName:1', 12)
('MyThreadName:1', 13)
('MyThreadName:1', 14)
('MyThreadName:1', 15)
('MyThreadName:1', 16)
('MyThreadName:1', 17)
('MyThreadName:1', 18)
('MyThreadName:1', 19)
('MyThreadName:1', 20)
('MyThreadName:2', 21)
('MyThreadName:2', 22)
('MyThreadName:2', 23)
('MyThreadName:2', 24)
('MyThreadName:2', 25)
('MyThreadName:2', 26)
('MyThreadName:2', 27)
('MyThreadName:2', 28)
('MyThreadName:2', 29)
('MyThreadName:2', 30)

'''