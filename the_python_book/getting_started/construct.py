#!/usr/bin/env python

import sys # Used for sys.exit function


TargetInt = input("How many integers?")

try:
    TargetInt = int(TargetInt)
except ValueError:
    sys.exit("You must enter an integer")

ints = list()
count = 0

while count < TargetInt:
    new_int = input("Please enter an integer {0}:".format(count+1))
    isInt = False
    try:
        new_int = int(new_int)
        isInt = True
    except:
        print("You must enter an integer")

    if isInt == True:
        ints.append(new_int)
        count += 1

print("Printing list using a for loop")
for x in ints:
    print(x)

print("Printing list using a while loop")
total = len(ints)
count = 0
while count < total:
    print(str(ints[count]))
    count += 1

