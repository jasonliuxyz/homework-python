#-*- encoding: utf-8 -*-
'''
queue队列：
分类：
	queue.Queue(maxsize=0) FIFO对象 先进先出
	queue.LifoQueue(maxsize=0) LIFO对象  后进后出
	queue.PriorityQueue(maxsize=0) 优先对象

1、线程安全的队列；
2、作用：用来在生产者和消费者线程之间的信息传递
3、定义：class Queue(maxsize=0) maxsize指明队列存放的数据个数上限，达到上限就会阻塞，小于或等于0表示无上限
4、常用方法：
	empty():队列为空，返回 True ，否则返回 False 
	full()：队列是满的返回 True ，否则返回 False
 	put(item, block=True, timeout=None)：将 item 放入队列
	get(block=True, timeout=None):从队列中移除并返回一个项目
	task_done():
	join()
'''


from queue import Queue

q = Queue()

for i in range(5):
	q.put(i)

while not q.empty():
	print(q.get())
