# encoding: utf-8 
'''
字典的keys()和items()可以进行并、交、差运算，（不需要转换成set）
1、字典的 keys() 方法返回一个展现键集合的键视图对象
2、字典的 items() 方法返回一个包含 (键，值) 对的元素视图对象
3、字典的values()不行，是因为值视图不能保证所有的值互不相同;所以需要将其先转换成set
'''

a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}
b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}

print(a.keys())  # 返回键视图对象
print(a.keys() - b.keys())  # 返回set集群对象
print(a.keys() & b.keys())
print(a.items() & b.items())
#print(a.values() - b.values())

s1 = set(a.values())
s2 = set(b.values())
print(s1 - s2)
