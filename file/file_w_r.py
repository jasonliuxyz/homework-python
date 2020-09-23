# -*- encoding: utf-8 -*-

#文件句柄f 
with open('/tmp/test.txt', 'w') as f:
	f.write('abc')

with open('/tmp/test.txt', 'r') as f:
	print(f.read())
