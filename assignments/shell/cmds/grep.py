#!/usr/bin/env python

def grep(file=None,keyword=None):
    if file is None or keyword is None:
        print("enter the format grep 'keyword' file name")    
    else:    
        search=open(file, 'r').read().find(keyword)
        if search is -1:
            print("not found")
        else:
            print("found")
    return;
