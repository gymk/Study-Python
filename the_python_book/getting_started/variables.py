#!/usr/bin/env python
hello_str="Hello World"

# Creating variables
hello_int = 123
hello_bool = True
hello_tuple = (12,21,44)
hello_list = ["Hello",'this','is',"a",'list']
print(hello_list)

# Another way of creating a list
hello_list = list()
hello_list.append("HEllo")
hello_list.append("this")
hello_list.append('is')
hello_list.append('a')
hello_list.append('string')
print(hello_list)

# Dictionary
hello_dict = {"first_name": 'YMK', "last_name":'G', 'eye_color':'black'}
print(hello_dict)

# playing with list and dict
print(hello_list[1])
print(hello_list[0]+"-WhatHappensNow")
print(hello_list)

hello_list[4] += "!!!"
print(hello_list)

print(hello_tuple)
print(hello_tuple[0])
print(hello_tuple[1])
print(hello_tuple[2])
print(str(hello_tuple))


print("{0} {1} has {2} eyes...".format(hello_dict['first_name'], hello_dict['last_name'], hello_dict['eye_color']))
