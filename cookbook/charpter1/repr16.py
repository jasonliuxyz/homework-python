#encoding: utf-8
'''
1、python对象都继承object，object有很多内置方法
2、__str__：将实例对象按照自定义的格式用字符串的形式显示出来
3、__repr__：如果用IDE软件操作，功能与__str__完全一样，都是实例可视化显示
'''

class Student():
	def __init__(self, id):
		self.id = id

	def __str__(self):
		print("我要可视化实例内容了")
		return "Student(%s)" % (self.id)

	def __repr__(self):
		print("我是repr")
		return "Student(%s)" % (self.id)
s = Student('1')
print(s)
