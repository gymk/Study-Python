#!/usr/bin/env python

'''
# http://anandology.com/python-practice-book/iterators.html

Using this as reference
'''


import sys

# read over all the files
# in each file reads line by line and yields thosee line
def catFiles(fileNames):
    for f in fileNames:
        for line in open(f):
            yield(line)

# returns a generator over lines object which yields if pattern is found in lines object
def grep(pattern, lines):
    return (line for line in lines if pattern in line)

# function which iterates over lines object and prints it content
def printLines(lines):
    for line in lines:
        print(line)

# Entry function for this python script
def start():
    pattern = sys.argv[1]
    fileNames = sys.argv[2:]
    lines = grep(pattern, fileNames)
    #lines = catFiles(fileNames)
    printLines(lines)
    pass

if __name__ == '__main__':
    start()
