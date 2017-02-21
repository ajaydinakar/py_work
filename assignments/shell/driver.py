#!/usr/bin/env python

""" ********Project Assignment -1*****************************************************
    program to implement the 
    code written in python
    execution command: python driver.py

"""
""" Team members:Ajay Dinakar Kandavalli,Saikiran Reddy Nagulapally,Thirupathi Reddy P
  

         @References :http://stackoverflow.com
                https://docs.python.org/2/library/os.html
   ***********************************************************************************
"""
from cmds import commands 
import threading
import sys
import os
import pwd
"""run_command function executes each command function when called through assosiating 
   each function with a new seperate thread

"""
def run_command(cmd,arg1=None,arg2=None):


    if arg1 is None and arg2 is None:
        t = threading.Thread(target=cmd)
    elif arg2 is None:
        t = threading.Thread(target=cmd,args=(arg1,))
    else:
        t = threading.Thread(target=cmd,args=(arg1,arg2))
    t.start()
    t.join()

if __name__ == '__main__':
    while True:
        print("give your shell command or type exit to exit")
       # print("% ")
       # line = sys.stdin.readline()
       # var=line.strip()
        var=raw_input("%")
        var=var.split(" ")
       
        #print(var)
   
        if len(var) < 1:
            print("give a command after % sign like %cat filename etc")
            sys.exit(0)
        if len(var) < 2:
            var.append(None)
            var.append(None)
 
        cmd =var[0]
        print(len(var))
        if cmd == 'ls':
            run_command(commands.ls,var[1])
        elif cmd == 'pwd':
            run_command(commands.pwd)
        elif cmd == 'cat':
            run_command(commands.cat,var[1])
        elif cmd == 'cd':
            run_command(commands.chgdir,var[1])

        elif cmd == 'cp':
            run_command(commands.cp,var[1],var[2])
        elif cmd == 'mv':
            run_command(commands.mv,var[1],var[2])
        elif cmd == 'rm':
            run_command(commands.rm,var[1])
        elif cmd == 'mkdir':
            run_command(commands.mkdir,var[1])
        elif cmd == 'rmdir':
            run_command(commands.rmdir,var[1])
        elif cmd == 'head':
            run_command(commands.hd,var[1])
        elif cmd == 'tail':
            run_command(commands.tail,var[1])
        elif cmd == 'exit':
            break;
            run_command(commands.exit)
        elif cmd == 'less':
            run_command(commands.less,var[1])
        elif cmd == 'grep':
            run_command(commands.grep,var[2],var[1])
        elif cmd == 'wc':
            run_command(commands.wc,var[1])
        elif cmd == 'sort':
            run_command(commands.sort,var[1])
        elif cmd == 'who':
            run_command(commands.who)
        elif cmd == 'history':
            run_command(commands.history)
        elif cmd == 'chmod':
            run_command(commands.chmod,var[1],var[2])

        elif '>' in var:
            run_command(commands.cat,var[1])

        elif '>>'in var:
            run_command(commands.cat,var[1])    
        elif '<' in var:
            run_command(commands.less,var[1])
    
        elif '|' in var:
            run_command(commands.less,var[1])
    
        elif '>' in var and 'cat' in var:
            run_command(commands.cat,var[1])

        else:
            print("give the command in the implementation list")
