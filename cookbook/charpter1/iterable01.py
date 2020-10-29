# -*- encoding: utf-8 -*-
from collections.abc import Iterable

'''
可迭代对象包含:
1、集合或序列类型，如str,list,dict,tuple,set
2、文件对象
3、在类中定义了__iter__()方法的对象

可迭代对象特点：
1、包含__iter__()方法
2、for循环遍历的时候，本质是将被遍历对象转换成迭代器，然后使用next()不断返回下一个值;
   所以当可迭代对象的__iter__()方法实现必须是正确的，例如下述代码;
   不然会返回TypeError: iter() returned non-iterator of type 'IterObj'报错，意思是iter()函数不能将‘非迭代器’类型转成迭代器;

3、分解
'''

print(isinstance('', Iterable))
print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance((), Iterable))
print(isinstance(set(), Iterable))

print('has __iter__:' + str(hasattr('', '__iter__')))

with open('/data/code/test.py', 'r') as f:
	print(isinstance(f, Iterable))

class Iterobj:
	def __init__(self):
		self.a = [1, 2, 3, 4, 5]

	def __iter__(self):
		return iter(self.a)

# 错误示范
#	def __iter__(self):
#		return self

it = Iterobj()
print(isinstance(it, Iterable))

for i in it:
	print(i)

a, b, c, d, e = it
print(a)
a, _, c, _, _ = it

