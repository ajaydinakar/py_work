#!/usr/bin/env python
import os

def ls(flag=None):
    if flag is None:
        list =os.listdir(os.getcwd())
        length =len(list)
        ls=''
        for i in range(length):
            ls=ls+list[i]+" "
        print(ls)
    elif flag=='-l':
        pass
    elif flag=='-a':
        pass
    elif flag=='-h':
        pass
    else:
        print("give flag -l or -a or -h")
    return;

