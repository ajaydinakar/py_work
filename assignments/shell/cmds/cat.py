#!/usr/bin/env python
import os
def cat(file):
    if file is None:   
        print("you didnt given the file name")
    else:
        with open(file, 'r') as fin:
            print (fin.read())

    return;
