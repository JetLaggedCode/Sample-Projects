#Snake Eyes 2

from random import randint

def die_roll():
    roll = randint(1,6)
    return roll

def sum_rolls():
    g = die_roll()
    h = die_roll()
    k = g + h
    return k



sevens = 0
for i in range(1000):
    r = sum_rolls()
    if r == 7 or r == 11:
        sevens += 1

print "%d out of 1000 rolls are 7 or 11." % (sevens)
