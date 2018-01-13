#!/usr/bin/env python

'''
# http://anandology.com/python-practice-book/iterators.html

Using this as reference
'''


import sys as sys

def cat_files(filenames):
    """
    read over all the files
    in each file reads line by line and yields thosee line
        :param filenames: an iterator to list of file names
    """
    print('--->catFiles {0}'.format(type(filenames)))
    for file in filenames:
        for line in open(file):
            yield line

def grep(pattern, filenames):
    """
    another version for test
        :param pattern: pattern to be searched over the files
        :param filenames: list of filenames
    """
    return (line for line in cat_files(filenames) if pattern in line)

def print_lines(lines):
    """
    function which iterates over lines object and prints it content
        :param lines:  an iterator over lines for printing
    """
    print('--->print_lines {0}'.format(type(lines)))
    for line in lines:
        print(line)

def start():
    """
    Entry function for this python script
    """
    pattern = sys.argv[1]
    filenames = list(sys.argv[2:])
    lines = grep(pattern, filenames)
    print('--->start {0}'.format(type(lines)))
    print_lines(lines)
    #lines = cat_files(filenames)
    #print(type(lines))
    #print_lines(lines)

if __name__ == '__main__':
    start()
