#!/usr/bin/env python

import random

cs_number = random.randint(1, 20)

print('Hi, I am thinking of a number between 1 and 20. Can you guess what it is?')

guessTaken = 0
for guessTaken in range(6):    # Max 6 tries
    guess = int(input())
    
    if guess < cs_number:
        print('Your guess is too low')
    
    if guess > cs_number:
        print('Your guess is too high')
    
    if guess == cs_number:
        break;

        
if guess == cs_number:
    print('You have guessed it correctly. Congrats !!!')
else:
    print('Nope. The number that I have guessed is ' + str(cs_number))