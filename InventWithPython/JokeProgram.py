#!/usr/bin/env python

# Have questions as keys, its answers as values for those keys
questions = {
     'What do you get when you cross a snowman with a vampire?' : 'Frostbite'
    , 'What do dentists call an astronuat\'s cavity' : 'A black hole'
}

# Loop over the question and show the answer
for question, answer in questions.items():
    print(question)
    value = input()
    # check case-insensitive
    if(answer.lower() in value.lower()):
        print('Correct. It is: ' + answer)
    else:
        print('No. It is: ' + answer)

print('Knock Knock')
input()
print('Who\'s there')
input()
print('Interrupting cow')
print('Interrupting cow wh-MOO')
