#!/usr/bin/env python

""" ******************************Project Assignment -1******************************
                       
                      program to implement the shell commands  
           
                      Note:code written in python
                      execution command: python driver.py
                      implementation:give the commands one by one after the % sign
                      geting out of shell:give "exit" command for quiting from shell                 

    Team members:Ajay Dinakar Kandavalli,Saikiran Reddy Nagulapally,Thirupathi Reddy P
  

    @References :http://stackoverflow.com
                 https://docs.python.org/2/library/os.html
               for colors  https://www.youtube.com/watch?v=TvOKST5A6kI
                 https://docs.python.org/2/library/shutil.html
                 https://docs.python.org/2/library/os.html @@used while doing ls function
   ***********************************************************************************
"""
from cmds import commands 
import threading
import sys
import os
from colorama import *
"""run_command function executes each command function when called through assosiating 
   each function with a new seperate thread

"""
def one_cmd(var,ret=None):  #This function calls  various functions that implement command function through threads
    var=var.split(" ")

    if len(var) < 1:
        print("give a command after % sign like %cat filename etc")
        sys.exit(0)
    elif len(var) < 2:
        var.append(None)
        var.append(None)

    cmd =var[0]
    if cmd == 'ls':
        run_command(commands.ls,var[1],)
    elif cmd == 'pwd':
        run_command(commands.pwd)
    elif cmd == 'cat':
        if len(var)==3:
            run_command(commands.cat,var[1],var[2])
        else:
            var.append(var[1])
            var[1]="one"
            run_command(commands.cat,var[1],var[2])

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
        run_command(commands.hd,var[1],ret)
    elif cmd == 'tail':
        run_command(commands.tail,var[1],ret)
    elif cmd == 'exit':
        return;
        run_command(commands.exit)
    elif cmd == 'less':
        run_command(commands.less,var[1])
    elif cmd == 'grep':
        if len(var)==3:
            run_command(commands.grep,var[2],var[1])
        else:
            print "wrong systax"
    elif cmd == 'wc':
        if len(var)==3:
            run_command(commands.wc,var[1],var[2])
        else:                          #make a dummy variable and send as parameter
            var.append(var[1])
            var[1]="one"
            run_command(commands.wc,var[1],var[2])
    elif cmd == 'sort':
        run_command(commands.sort,var[1])
    elif cmd == 'who':
        run_command(commands.who)

    elif cmd == 'history':
        run_command(commands.history)
    elif cmd == 'chmod':
        run_command(commands.chmod,var[1],var[2])
    elif '!' in cmd:
        run_command(commands.hiscmd,var[0])

    else:
        print("give the command in the implementation list")
    return;
# the threading function run_command
def run_command(cmd,arg1=None,arg2=None):


    if arg1 is None and arg2 is None:
        t = threading.Thread(target=cmd) #for functions with no arguments
    elif arg2 is None:
        t = threading.Thread(target=cmd,args=(arg1,)) #for functions with one argument
    else:
        t = threading.Thread(target=cmd,args=(arg1,arg2)) #for function with two argument
    t.start()
    t.join()

if __name__ == '__main__':
    while True:
        print("give your shell command or type exit to exit")

        line=raw_input(Fore.GREEN+"% "+Fore.RESET)          #take the line command from user
        hist=open('/root/history.txt','a')  # store the command in history
        hist.write(line)
        hist.write('\n')
        hist.close()
        if line == 'exit':   #if exit terminate the loop
            break

        if '|' in line:
            line=line.split(' | ') #if | found split the line to idividual commands
            np=open("/root/mail.txt","w")
            np.write("hey dude (function) iam from main please dont print ")
            np.close()      
            one_cmd(line[0])
            for i in range(len(line[1:])):#loop for each inividual command
                fin=open("temp.txt","r")  #open the file which stores the first operand result
                read =fin.read()
                fout=open("temp2.txt","w")
                out=fout.write(read)
                line[i+1]=line[i+1]+" "+'temp2.txt'
                fout.close()
                one_cmd(line[i+1])
           
                fin.close()
            out=open("temp.txt","r")
            print out.read()
            np=open("/root/mail.txt","w")
            np.seek(0)
            np.truncate()
            np.close()
            out.close()
        elif '>>' in line:
            line = line.split(' >> ')
            np=open("/root/mail.txt","w")
            np.write("garbage") # size of this file tells when to print
            np.close()
            one_cmd(line[0])
            fin=open("temp.txt","r")
            fout=open(line[1],"a")      
            read=fin.read()
            out=fout.write(read)
            fin.close()
            fout.close()
            np=open("/root/mail.txt","w")
            np.seek(0)
            np.truncate()
            np.close()            
        
        elif '>' in line:
            line=line.split(' > ')
            np=open("/root/mail.txt","w")
            np.write("garbage")              #size of the file tells when to print
            np.close()
            one_cmd(line[0])
            fin=open("temp.txt","r")
            fout=open(line[1],"w")
            read=fin.read()
            out=fout.write(read)
            fin.close()
            fout.close()
            np=open("/root/mail.txt","w")
            np.seek(0)
            np.truncate()
            np.close()
        elif '<' in line:
            line=line.split(' < ')
            line=line[0]+" "+line[1]
            one_cmd(line)
    
        else:    
            one_cmd(line)


