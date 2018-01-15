#!/usr/bin/env python

import sys

def my_grep(pattern,filenames):
    print('Searching for {0} in {1}'.format(pattern, filenames))
    for f in filenames:
        for line in open(f):
            if pattern in line:
                sys.stdout.write(line)
                #print(line)
    sys.stdout.flush()

def start():
    print(sys.argv[1])
    print(sys.argv[2:])
    my_grep(sys.argv[1], sys.argv[2:])

if __name__ == '__main__':
    start()
