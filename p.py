#!/usr/bin/env python
import os
import sys
import shutil
import linecache
from shutil import copyfile
def ls(arg=None):
    cmd="ls"
    if arg is None:
        os.system(cmd)
    else:
        os.system(cmd+" "+arg)
    return;
def head(file=None):
    if file is None:
        print("err :must enter the file name after head command ")
    else:     
        f=open(file)
        for i in range(10):
            line=f.next().strip()
            print (line)
        f.close()
    return;
def cd(file):
    
var=input()
var=var.split(" ")
print (var)
cmd=var[0]
if cmd == 'ls':
    ls(var[1])

elif cmd == 'head':
    head(var[1])
elif cmd == 'cd':
    cd(var[1])
