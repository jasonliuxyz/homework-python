#encoding: utf-8 
'''
0、sorted(iterable, /, *, key=None, reverse=False)
1、sorted函数能对所有可迭代对象进行排序，结果返回一个列表
2、可以自定义key函数，用来指定在进行比较前要在每个列表元素上调用的函数
3、reverse能降序
'''
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)


def sort_notcompare():
    users = [User(23), User(3), User(99)]
    print(users)
    print(sorted(users, key=lambda u: u.user_id))
sort_notcompare()
