import urllib
from urllib import request
# python3 里urllib2不再可用

url_path = 'http://pwxa2lbiz.bkt.clouddn.com/ae9b85156eee33d9536ad8ca5152861e.png'

f = request.urlopen(url_path)
with open('demo.png', 'wb') as fo:
    fo.write(f.read())
