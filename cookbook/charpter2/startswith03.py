'''
1、str.endswith(...) 
	可以传入单个字符串，也可以传入tuple
2、startswith(...)
	
'''

filename = 'spam.txt'

print(filename.endswith('txt'))
print(filename.startswith('spam'))

import os
filenames = os.listdir('.')

list = [ filename for filename in filenames if filename.endswith(('.py', '.txt'))]
print(list)
