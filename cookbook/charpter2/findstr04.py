'''
'''

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.find('no'))

import re
text1 = '11/27/2012'
print(re.match(r'\d+\/\d+\/\d+', text1))

datepat = re.compile(r'\d+/\d+/\d+')

