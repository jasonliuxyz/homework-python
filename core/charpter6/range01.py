'''
python3和python2下range()区别：
1、python2 range返回list
2、python3 range返回迭代值，要生成list，就要用list()函数
'''

a='abcde'
for i in [None] + list(range(-1, -len(a), -1)):
	print(a[:i])

