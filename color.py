#!/usr/bin/env python
import os
from colorama import *
def color(f):
    if os.path.isdir(f) == True:
        return Fore.BLUE+f+Fore.RESET
    else:
        return f
def colum(f):
    colum=6
    for count, item in enumerate(sorted(f), 1):
        if os.path.isdir(item) == True:
            print Fore.BLUE+item.ljust(20)+Fore.RESET,
        else:
            print  item.ljust(20),
        if count % colum == 0:
            print




list=os.listdir('.')
colum(list)
