#!/usr/bin/env python

import random

words = '''ant baboon badger bat bear beaver camel cat clam cobra cougar
       coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk
       lion lizard llama mole monkey moose mouse mule newt otter owl panda
       parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep
       skunk sloth snake spider stork swan tiger toad trout turkey turtle
       weasel whale wolf wombat zebra'''.split()

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
        s += c
        s += ' '

    print(s)
    return


def display_hangman(word, guessed_letters, missed_count, missed_letters):
    print(hangman_pics[missed_count])
    print('Missed letters: ' + missed_letters)
    s = getGuessedString(word, guessed_letters)
    printGuessedString(s)
    return
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

    word_index = random.randint(0, len(words)-1)
    word = words[word_index]

    guessed_letters = ''
    missed_letters = ''
    missed_count = 0
    while(missed_count < len(hangman_pics)-1 and len(word) > 0):
        display_hangman(words[word_index], guessed_letters, missed_count, missed_letters)
        print('Guess a letter')
        guess = getUserGuess()
        if(isLetterInWord(guessed_letters, guess)):
           print('You have already guessed that letter. Choose again.')
           continue
        if(isLetterInWord(word, guess)):
            guessed_letters += guess
            word = word.replace(guess, '')
            continue;
        if(isLetterInWord(missed_letters, guess)):
            print('You have already guessed that letter. Choose again.')
            continue
        missed_letters += guess
        missed_count += 1
        #display_hangman(word, guessed_letters, missed_count, missed_letters)

    if len(word) == 0:
        print('Yes! The secret word is \"' + words[word_index] + '\"! You have won!')
    else:
        display_hangman(words[word_index], guessed_letters, missed_count, missed_letters)
        print('You missed it. It is \"' + words[word_index] + '\"');

    print('Do you want to play again? (yes or no)')
    playAgain = input()
       
       
