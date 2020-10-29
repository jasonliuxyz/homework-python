#encoding: utf-8 
'''
1、切片对象slice()
2、切片对象属性
	2.1、slice.start | stop | step 获取切片的属性
3、indices(size)将它映射到一个已知大小的序列上
'''

s = slice(0, 3)
items = [0, 1, 2, 3, 4, 5, 6]
print(items[s])

print(s.start)

s = slice(0, 10)
print(s.indices(len(items)))
