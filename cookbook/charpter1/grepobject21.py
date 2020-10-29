#encoding: utf-8

'''
过滤列表元素
1、通过列表生成式
2、通过生成器
3、通过filter()函数
4、itertools.compass()函数
'''

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
greplist = [i for i in mylist if i > 0]
print(greplist)

a = [i if i > 0 else 0 for i in mylist]
print(a)

greplistgen = (i for i in mylist if i > 0)
for i in greplistgen:
	print(i)

def is_int(i):
	try:
		x = int(i)
		return True
	except ValueError:
		return False

values = ['1', '2', '-3', '-', '4', 'N/A', '5']
ivals = filter(is_int, values)
for i in ivals:
	print(i)


