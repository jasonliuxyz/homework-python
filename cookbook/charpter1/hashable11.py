#encoding: utf-8
'''
1、消除重复元素的同时，保持元素顺序位置
'''

a = [1, 5, 2, 1, 9, 1, 5, 10]
print(set(a))

def hashable(items):
	s = set()
	for item in items:
		if item not in s:
			yield item
			s.add(item)

print(list(hashable(a)))

d = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
#print(set(d))

def dedupe(items, key=None):
	s = set()
	for item in items:
		val = item if key is None else key(item)
		if val not in s:
			yield item
			s.add(val)

print(list(dedupe(d, key=lambda d: (d['x'],d['y']))))

with open(r'/data/code/test.txt', 'r') as f:
	for line in hashable(f):
		print(line, end='')
