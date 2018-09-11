#!/usr/bin/env python

import random
import time

def displayIntro():
    print('''You are in a land full of dragons. In front of you,
you see two caves. In one cave, the dragon is friendly
and will share his treasure with you. The other dragon'
is greedy and hungry, and will eat you on sight.
Which cave will you go into (1 or 2)''')


def getCaveSelection():
    user_selection = ''
    while True:
        if(user_selection == '1' or user_selection == '2'):
            break;
        # probably invalid input. read again from user
        user_selection = input()
       
    return user_selection

def checkCave(chosenCave):
    print('You approach the cave')
    time.sleep(2)
    print('It is dark and spooky')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and ...')
    time.sleep(2)
    
    friendlyCave = random.randint(1,2)
    if(int(chosenCave) == friendlyCave):
        print('Gives you his treasure')
    else:
        print('Gobbles you down in one bite')
    return

playAgain = 'Yes'
while playAgain == 'yes' or playAgain == 'Yes' or playAgain == 'y' or playAgain == 'Y':
    displayIntro()
    selectedCave = getCaveSelection()
    checkCave(selectedCave)
    
    print('Do you want to play the game again? (yes or no)')
    playAgain = input()

print('Bye!!!')
