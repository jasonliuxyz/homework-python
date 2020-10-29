#encoding: utf-8

import requests

url = 'http://www.baidu.com'

r = requests.get(url)
#print(r.text)

url = 'http://httpbin.org/get'
d = {'k1':'v1'}
r = requests.get(url, params = d)
print(r.text)
