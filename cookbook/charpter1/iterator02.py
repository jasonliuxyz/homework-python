# -*- encoding: utf-8 -*-

'''
迭代器:
1、可迭代对象包含迭代器，所以迭代器中实现了__iter__方法
2、迭代器比可迭代对象要对实现__next__方法
3、iter()函数将一个可迭代对象转成迭代器对象

迭代器作用：
迭代器是实现了迭代器协议的数据结构，通过迭代器来屏蔽底层的复杂逻辑
参考：https://drivingc.com/p/5c4c210d4b0f2b793a5fe2e7
'''
from collections.abc import Iterable
from collections.abc import Iterator
from collections.abc import Generator
class IterObj:
	def __init__(self):
		self.a = [3, 5, 7, 11, 13, 17, 19]

		self.n = len(self.a)
		self.i = 0
	def __iter__(self):
		return iter(self.a)

	def __next__(self):
		while self.i < self.n:
			v = self.a[self.i]
			self.i += 1
			return v
		else:
			self.i = 0
			raise StopIteration()

it = IterObj()
print(isinstance(it, Iterable))
print(isinstance(it, Iterator))
print(isinstance(it, Generator))
print(hasattr(it, "__iter__"))
print(hasattr(it, "__next__"))

print(next(it))
print(next(it))
print(next(it))

with open('/data/code/test.py', 'r') as f:
	print(isinstance(f, Iterator))	
