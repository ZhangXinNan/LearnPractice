
import threading

def worker(num, results, i):
    '''thread Worker function'''
    print 'Worker: %s' % num
    results[i] = num * 10

threads = []
results = [None] * 5
for i in range(5):
    t = threading.Thread(target=worker, args=(i, results, i))
    threads.append(t)
    t.start()

print results