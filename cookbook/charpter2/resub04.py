'''
'''

import re
text1 = 'UPPER PYTHON, lower python, Mixed Python'
text2 = 'Today is 11/27/2012. PyCon starts 3/13/2013.'

#print(re.sub(r'PYTHON', 'a', text, flags=re.IGNORECASE))
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
strpat = re.compile('python')

def matchcase(word):
	def change(m):
		text = m.group()
		if text.isupper():
			return word.upper()
		elif text.islower():
			return word.lower()
		elif text[0].isupper():
			return word.capitalize()
		else:
			return word
	return change
#print(strpat.sub(matchcase('a'), text1), flags=re.IGNORECASE)
print(re.sub('python', matchcase('snake'), text1, flags=re.IGNORECASE))

def change(m):
	return '{} {} {}'.format(m.group(3), m.group(1), m.group(2))

print(datepat.sub(change, text2))	
