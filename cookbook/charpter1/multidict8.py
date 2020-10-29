from collections import defaultdict

'''

'''

pairs = {'a':1, 'b':2}
d = defaultdict(list)
for key, value in pairs.items():
	d[key].append(value)
print(d)
