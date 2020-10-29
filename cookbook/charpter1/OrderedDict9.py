from collections import OrderedDict
'''
OrderedDict特点
1、保持元素被插入时的顺序
2、大小是一个普通字典的两倍，内部维护着另外一个链表
3、根据键插入顺序排序的双向链表
4、每次当一个新的元素插入进来的时候， 它会被放到链表的尾部
'''

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
for key in d:
    print(key, d[key])
