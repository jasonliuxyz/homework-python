import heapq
'''
堆定义
1、是一个完全二叉树，可分为最大堆和最小堆(父节点是否大于所有子节点)
2、使用heapq最大好处就是第一个节点一定是最小元素

堆创建
1、使用python内建的名为heapq的库创建
2、heapify - 此函数将常规列表转换为堆
3、heappush - 这个函数在堆中添加一个元素而不改变当前堆
3、heappop - 该函数返回堆中最小的数据元素
4、heapreplace - 该函数用函数中提供的新值替换最小的数据元素

堆使用
1、查找最小或最大的 N 个元素，并且 N 小于集合元素数量，使用heapq.nsmallest()和heapq.nlargest()
2、想查找唯一的最小或最大（N=1）的元素的话，那么使用 min() 和 max() 函数
3、查找最小或最大的 N 个元素，如果 N 的大小和集合大小接近的时候，先排序这个集合然后再使用切片操作，sorted(items)[:N]
'''

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nsmallest(3, nums))

a = sorted(nums)[:10]
print(a)
