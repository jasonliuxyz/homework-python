from fighter import Figher
from random import randint, randrange

class Monster(Figher):
    __slots__ = ('_name', '_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
               '生命值: %d\n' % self._hp
