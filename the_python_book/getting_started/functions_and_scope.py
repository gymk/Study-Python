#!/usr/bin/env python

def modify_string(original):
    original += " that has been modified"

def modify_string_return(original):
    original += " that has been actually modified"
    return original

test_string = "This is my test string"

modify_string(test_string)
print(test_string)

test_string = modify_string_return(test_string)
print(test_string)