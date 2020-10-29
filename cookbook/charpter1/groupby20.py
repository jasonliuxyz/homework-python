#encoding: utf-8
'''
1、groupby() 仅仅检查连续的元素，如果事先并没有排序完成的话，分组函数将得不到想要的结果
2、groupby() 函数扫描整个序列并且查找连续相同值（或者根据指定 key 函数返回值相同）的元素序列
'''

rows = [
    {'address': '5412 N CLARK', 'date': '07/01/2012'},
    {'address': '5148 N CLARK', 'date': '07/04/2012'},
    {'address': '5800 E 58TH', 'date': '07/02/2012'},
    {'address': '2122 N CLARK', 'date': '07/03/2012'},
    {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
    {'address': '1060 W ADDISON', 'date': '07/02/2012'},
    {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
    {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]

from operator import itemgetter
from itertools import groupby

rows.sort(key=itemgetter('date'))

for date, items in groupby(rows, key=itemgetter('date')):
	print(date)
	for i in items:
		print(' ', i)
