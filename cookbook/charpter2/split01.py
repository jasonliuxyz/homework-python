#encoding: utf-8

'''
split(self, /, sep=None, maxsplit=-1)
split是字符串内置函数
按照指定的符号sep来对字符串进行切割，默认的分隔符为所有的空字符，包括空格、换行(\n)、制表符(\t)等
'''

str1 = 'Line1-abcdef \nLine2-abc \nLine4-abcd';
print(str1.split())
print(str1.split(maxsplit=2))

print(str1.rsplit(maxsplit=1))


