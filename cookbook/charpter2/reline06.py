import re

text2 = '''/* this is a
multiline comment */'''

#l = re.findall(r'/\*((?:.|\n)*)\*/', text2) 
l = re.findall(r'/\*([\s\S]*?)\*/', text2)
print(l)
