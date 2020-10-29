#encoding: utf-8

'''
1、dict中x.__getitem__(y) <==> x[y]
2、operator 模块的 itemgetter 函数比上面的稍微快些
'''

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

print(sorted(rows, key = lambda x : x.__getitem__('uid')))
print(sorted(rows, key = lambda x : x['uid']))

from operator import itemgetter
print(sorted(rows, key=itemgetter('fname')))
