import re
text2 = 'Computer says "no." Phone says "yes."'
print(re.findall(r'"(.*?)"', text2))
