#encoding: utf-8
'''
命名元组
1、通过名称来访问元素，含有tuple所有特点, 代替普通tuple使用下标来访问
2、_replace()创建一个全新的命名元组并将对应的字段用新的值取代
'''

from collections import namedtuple

Animal = namedtuple('Animal', 'name age type')
big_yellow = Animal(name="big_yellow", age=3, type="dog")
print(big_yellow)

#big_yellow.age += 1
#print(big_yellow)

big_yellow = big_yellow._replace(age = 4)
print(big_yellow)

name, age, type = big_yellow
print(name, age, type)

p = namedtuple('p', ['name', 'age', 'addr'])
liu = p('jason', 27, 'shanghai')
print(liu)
