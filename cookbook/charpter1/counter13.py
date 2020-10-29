#encoding: utf-8

'''
1、查找序列中出现次数最多的元素
2、Counter(iterable=None, /, **kwds)统计可hashable的列表，返回一个字典对象
3、most_common() 返回最大值
4、Counter对象能跟数学运算操作相结合
'''

words = [
    'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]
morewords = ['why','are','you','not','looking','in','my','eyes']

d = {}
for item in words:
	d[item] = d.get(item, 0) + 1

sorted_dict = sorted(zip(d.values(), d.keys()), reverse=True)
print(max(sorted_dict))

from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

print(word_counts['look'])

a = Counter(words)
b = Counter(morewords)
print(a+b)
