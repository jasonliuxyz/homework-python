#enconding: utf-8

'''
re模块两种使用方式：
	复用正则规则：
		1、patter = re.compile(r'') 生成patter对象
		2、m = patter.match(str) 通过patter的一系列方法对文本进行匹配查找
		方法：
 match		match(string[, pos[, endpos]]) 查找字符串的头部（也可以指定起始位置）
 match		search(string[, pos[, endpos]]) 查找字符串的任何位置
		findall(string[, pos[, endpos]]) 以列表形式返回全部能匹配的子串
		finditer()string[, pos[, endpos]] 以迭代器形式返回全部能匹配的子串
		split(string[, maxsplit]) 按照能够匹配的子串将字符串分割后返回列表
		sub(repl, string[, count]) 替换
		subn(repl, string[, count]) 返回一个元组
	直接使用：
		1、re模块本身提供很多方法对文本进行匹配操作
	两者返回match对象包含的方法：
		group([group1, …]) 获得一个或多个分组匹配的字符串，整个匹配的子串时，可直接使用 group() 或 group(0)
		start([group]) 获取分组匹配的子串在整个字符串中的起始位置
		end([group]) 获取分组匹配的子串在整个字符串中的结束位置
		span([group]) 方法返回 (start(group), end(group))
	
1、re.split中如果使用()捕获分组，那么被匹配的文本也将出现在结果列表中
2：re.match(pattern, string[, flags]) 查找字符串头部
'''
import re

line = 'asdf fjdk;; afed, fjek,asdf,  foo'
print(re.split(r'[;,\s]+', line))

print(re.split(r'((;|,|\s)\s?)', line))

url = 'http://www.python.org'
m = re.match(r'http|https|ftp', url)
print(m.group())

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'
if re.match(r'\d+/\d+/\d+', text1):
	print('yes')
else:
	print('no')

if re.match(r'\w+\s\d+,\s\d+', text2):
	print('yes')
else:
	print('no')


datapat = re.compile(r'\d+/\d+/\d+')
if datapat.match(text1):
	print('yes')
else:
	print('no')

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datapat.findall(text))

m = datapat.search(text)
print(m.group())
#print(m.group(1))

datapat = re.compile(r'(\d+)/(\d+)/(\d+)')
m = datapat.findall(text)
#print(m.group(1))
#print(m.span())

print(datapat.sub(r'\3-\1-\2', text))
