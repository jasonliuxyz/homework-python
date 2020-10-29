#encoding: utf-8

'''
'''

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)

u = User('1')
print(u.__getattribute__('user_id'))
