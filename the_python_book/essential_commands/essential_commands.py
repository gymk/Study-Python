#!/usr/bin/env python

# ====> Modules
from importlib import *
import sys as st

print(st.api_version)

print(st.copyright)

# Reloading Modules
print("before reloading...")
reload(st)
print("after reloading...")

print(st.api_version)

print(st.copyright)

'''
# ====> Executin Scripts

Executing python scripts from a pything script
Note that only python scripts can be executed in this way
'''
exec(open("/home/kyuties/Study/python/the_python_book/getting_started/variables.py").read())

# Below trial fails, because it is a bash script, not a python script
#
#   #!/bin/sh
#
#   ls -la
#exec(open("/home/kyuties/Study/python/the_python_book/essential_commands/list_files.sh").read())


'''
# ====> Evaluating Code

Note that it uses current session while evaluating the python commands
For example if a undefined variable is found inside eval() script
it will report error
'''
eval("print(1)")
av = 'ttt'
eval("print(av)")


'''
# ====> Asserting Values
'''

assert(True == True)
assert(True != False)
# Below command generates assertion
#assert(True == False)


'''
# ====> Mapping Functions

map(aFunction, aSequence)
'''

# Normal way of computation
items = [1,2,3,4,5]
squared = list()
for x in items:
    squared.append(x**2)
print(squared)

# Same computation using map
def my_sqr(x):
    return x**2

print(list(map(my_sqr,items)))

'''
# ====> Lambda Functions

Mostly lamba used in expression oriented programming
Following are the expression oriented programming in Python

1) map(aFunction, aSequence)
2) filter(aFunction, aSequence)
3) reduce(aFunction, aSequence)
4) lambda
5) list comprehension
'''
# Same squaring using map and lamba
print(list(map((lambda x: x**2), items)))

# List of functions
def my_cube(x):
    return x**3

funcs = [my_sqr, my_cube]
for r in range(10):
    value = list(
        map(
            (lambda x: x(r)), funcs
            )
    )
    print(value)