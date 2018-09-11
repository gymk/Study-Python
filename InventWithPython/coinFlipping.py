#!/usr/bin/env python

import random

print('I am going to flip a coin 1000 times. Guess how many times it will come up with heads? (Press ENTER to begin)')
input()

heads = 0
for flips in range(1,1001):
    if(random.randint(0,1) == 1):
        heads += 1
    if (flips % 100 == 0):
        print(str(flips) + ' till now and there have been ' + str(heads) + ' heads')

print()
print('Out of 1000 tosses, heads came up ' + str(heads) + ' times')
print('Were you close?')
