#!/usr/bin/env python
import os
def chgdir(arg=None):
    
    if arg is None or arg is '~':
        os.chdir('/home/')               #change directory to home
        print("you are in home dir ")
    elif arg is '..':
        os.chdir('..')
    else:
        os.chdir(arg)                    #change directory to specific location
    return;
