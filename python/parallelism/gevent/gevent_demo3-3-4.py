import gevent.monkey
gevent.monkey.patch_socket()

import gevent
# python2
# import urllib2
# python3
import urllib.request
import json

def fetch(pid):
    # python2
    # response = urllib2.urlopen('http://json-time.appspot.com/time.json')
    # python3
    response = urllib.request.urlopen('http://json-time.appspot.com/time.json')
    result = response.read()
    json_result = json.loads(result)
    datetime = json_result['datetime']

    print('Process %s: %s' % (pid, datetime))
    return json_result['datetime']

def synchronous():
    for i in range(1,10):
        fetch(i)

def asynchronous():
    threads = []
    for i in range(1,10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

print('Synchronous:')
synchronous()

print('Asynchronous:')
asynchronous()
