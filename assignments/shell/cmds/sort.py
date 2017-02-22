#!/usr/bin/env python
import sys
def sort(file):
    f = open(file )
    lines = f.readlines()
    lines.sort()
    map(sys.stdout.write, lines) #prints the sorted list
    f.close()

    return;


