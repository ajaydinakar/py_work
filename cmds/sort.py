#!/usr/bin/env python
#@function sort
#takes input from a file and displays the sorted list of lines 
import sys
def sort(file):
    f = open(file )
    lines = f.readlines()
    lines.sort()
    map(sys.stdout.write, lines) #prints the sorted list
    f.close()

    return;


