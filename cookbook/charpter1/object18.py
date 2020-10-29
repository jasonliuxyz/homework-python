#encoding: utf-8

'''
1、dir(object) 返回 object 的有效属性列表
2、对象具有名为 __dir__() 的方法，则将调用此方法，并且必须返回属性列表
'''

d = {'a':1, 'b':2}
#print(dir(d))

class Student():
	def __init__(self, name):
		self.name = name

	def __dir__(self):
		return ['area', 'perimeter', 'location']

	def __getattribute__(self, attr):
#		return object.__getattribute__(self, attr)
		return('test')

	def __getattr__(self, attr):
		return '访问成员不存在'
		
s = Student('liu')
print(dir(s))
print(getattr(s, 'name'))
print(s.__getattribute__('name'))
print(s.id)
print(s.name)
