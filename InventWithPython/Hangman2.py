#!/usr/bin/env python

import random

words = {
    'animals' : '''ant baboon badger bat bear beaver camel cat clam cobra cougar
   coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
   lion lizard llama mole monkey moose mouse mule newt otter owl panda
   parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
   skunk sloth snake spider stork swan tiger toad trout turkey turtle
   weasel whale wolf wombat zebra'''.split(),

   'colors' : '''red orange yellow green blue purple indigo violet whilte black
        brown'''.split(),
   
    'shapes' : '''square triangle rectangle circle ellipse rhombus trapezoid
            chevron pentagon hexagon septagon octagon'''.split(),
    
    'fruits' : '''apple orange lemon lime pear watermelon grape grapegruit cherry
            banana cantaloupe mango strawberry tomato'''.split()
    }


hangman_pics = ['''
    +---+
        |
        |
        |
    ======''','''
    +---+
    O   |
        |
        |
    ======''','''
    +---+
    o   |
   /    |
        |
    ======''','''
    +---+
    O   |
   /|   |
        |
    ======''','''
    +---+
    O   |
   /|\  |
        |
    ======''','''
    +---+
    O   |
   /|\  |
   /    |
    ======''','''
    +---+
    O   |
   /|\  |
   / \  |
    ======'''
,'''
    +---+
   [O   |
   /|\  |
   / \  |
    ======''','''
    +---+
   [O]  |
   /|\  |
   / \  |
    ======'''
]

def isLetterInWord(word, char):
    if(char in word):
        return True;
    return False;

def getUserGuess():
    while True:
        letter = input()
        if len(letter) != 1:
            continue
        if not letter.isalpha():
            continue
        return letter.lower()
    

def getGuessedString(word, guessed_letters):
    s = ''
    for c in word:
        if c in guessed_letters:
            s += c
        else:
            s += '_'
    return s

def printGuessedString(guessed_string):
    s = ''
    for c in guessed_string:
        s += c+' '

    print(s)
    return


def display_hangman(word, guessed_letters, missed_count, missed_letters):
    print(hangman_pics[missed_count])
    print('Missed letters: ' + missed_letters)
    s = getGuessedString(word, guessed_letters)
    printGuessedString(s)
    return

def getRandomWord(words_dict):
    word_key = random.choice(list(words_dict.keys()))
    word = random.randint(0, len(words_dict[word_key])-1)
    return word_key, words_dict[word_key][word]

'''
print(len(hangman_pics))
for pic in hangman_pics:
    print(pic)

print(len(words))
for word in words:
    print(word)
'''

playAgain = 'Yes'
while playAgain == 'Yes' or playAgain == 'yes' or playAgain == 'Y' or playAgain == 'y':
    print('H A N G M A N')
    print()
    
    word_category, word = getRandomWord(words)
    
    letters = ''.join(set(word))

    guessed_letters = ''
    missed_letters = ''
    missed_count = 0
    while(missed_count < len(hangman_pics)-1 and len(guessed_letters) < len(letters)):
        print()
        print('The secre word is in the set: ' + word_category)
        display_hangman(word, guessed_letters, missed_count, missed_letters)
        print('Guess a letter')
        guess = getUserGuess()
        if(guess in guessed_letters or guess in missed_letters):
           print('You have already guessed that letter. Choose again.')
           continue
        if(guess in word):
            guessed_letters += guess
            continue;
        missed_letters += guess
        missed_count += 1
        #display_hangman(word, guessed_letters, missed_count, missed_letters)

    if len(word) == 0:
        print('Yes! The secret word is \"' + word + '\"! You have won!')
    else:
        display_hangman(word, guessed_letters, missed_count, missed_letters)
        print('You missed it. It is \"' + word + '\"');

    print('Do you want to play again? (yes or no)')
    playAgain = input()
       
       
