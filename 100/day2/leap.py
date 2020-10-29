year = int(input('请输入年份:'))
# 运算符的优先级、括号改变运算符的优先级
is_leap = (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)
print(type(is_leap))
print(is_leap) 
