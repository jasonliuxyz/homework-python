# -*- encoding: utf-8 -*-

'''
生成器实现方式：
1、yield生成器函数
2、列表生成器

生成器特点：
0、一边循环一边计算的机制，称为生成器（不占用大量空间）
1、属于迭代器一种
2、可迭代对象
3、包含特殊方法:send(), throw(), close()
'''
from collections.abc import Generator
from collections.abc import Iterator
from collections.abc import Iterable 

def gen():
	i = 0
	while i<10:
		yield i
		i+=1

print(isinstance(gen(), Generator))

ff = gen()
for a in ff:
	print(a)

g = (x * 2 for x in range(10))
print(isinstance(g, Generator))

print(isinstance(g, Iterator))
print(isinstance(g, Iterable))
print(hasattr(g, '__iter__'))
print(hasattr(g, '__next__'))
