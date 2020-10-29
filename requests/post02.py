#encoding: utf-8 
'''
1、post dict对象
2、post json字符串
'''

import json
import requests
payload = {'key1': 'value1', 'key2': 'value2'}

ret = requests.post("http://httpbin.org/post", data=payload)

print(ret.text)


payload = {'some': 'data'}
url = 'http://httpbin.org/post'
#headers = {'content-type': 'application/json'}
#ret = requests.post(url, data=json.dumps(payload), headers=headers)
#ret = requests.post(url, data=json.dumps(payload))
#ret = requests.post(url, json=json.dumps({'some': 'data'}))
ret = requests.post(url, data=json.dumps({'some': 'data'}))

print(ret.text)


