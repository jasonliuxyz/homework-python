# -*- encoding: utf-8 -*-
'''
deque特点
1、deque在两端高效实现插入和删除操作；适用于队列和栈
2、在两端高效插入和删除是靠appendleft()和popleft()方法,append()和pop()方法

deque用法：
1、deque(maxlen=N) 构造函数会新建一个固定大小的队列。当新的元素加入并且这个队列已满的时候， 最老的元素会自动被移除掉
2、不设置最大队列大小，那么就会得到一个无限大小队列
3、新增append()和appendleft()
4、删除pop()和popleft()
5、扩展extend()和extendleft()

参考：https://zhuanlan.zhihu.com/p/32201189
'''

from collections import deque

d = deque(maxlen=5)
for i in range(8):
	d.append(i)

print(d)
for a in d:
	print(a)
