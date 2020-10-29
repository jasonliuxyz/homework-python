# encoding: 'utf-8'

'''
对字典进行计算，一般是要对value进行计算；
为了对字典值执行计算操作，通常需要使用 zip() 函数先将键和值反转过来；
zip() 函数创建的是一个只能访问一次的迭代器
如果字典恰巧最小或最大值有重复的，那么拥有最小或最大键的实体会返回
'''
prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

print(zip(prices.values(), prices.keys()))
print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))

for key, value in zip(prices.values(), prices.keys()):
	print(key, value)

print(sorted(zip(prices.values(), prices.keys())))

# key是蒋price字典中的key依次作为参数传给lambda函数
print(min(prices, key=lambda k: prices[k]))
