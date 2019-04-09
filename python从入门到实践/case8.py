from collections import OrderedDict
from random import randint

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print name.title() + "'s favorate language is " + \
          language.title() + "."

print randint(1, 6)


class Die(object):
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print randint(1, self.sides)


die1 = Die(6)
for i in range(10):
    die1.roll_die()
print '--------------'
die2 = Die(10)
for i in range(10):
    die2.roll_die()
