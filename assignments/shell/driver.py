#!/usr/bin/env python
from cmds import commands 
import threading
import sys

def run_command(cmd,args=None,flags=None):

    if args:
        t = threading.Thread(target=cmd, args=(args,))
    else:
        t = threading.Thread(target=cmd)
        
    t.start()
    t.join()

if __name__ == '__main__':

    var=input('%')
    var=var.split(" ")
    print(var)
   
    if len(var) < 1:
        print("usage: python driver.py cmd where cmd = 'ls' or 'pwd', etc.")
        sys.exit(0)
 
    cmd =var[0]
    print(len(var))
    if cmd == 'ls':
        run_command(commands.ls,var[1])
    elif cmd == 'pwd':
        run_command(commands.pwd)
    elif cmd == 'cat':
        run_command(commands.cat,var[1])
