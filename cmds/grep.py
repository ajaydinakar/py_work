#!/usr/bin/env python
"""@function name:grep
   finds a word in a file and return the line where the word is found
"""
import os
from colorama import *
def grep(file=None,keyword=None):
    if file is None or keyword is None:
        print("enter the format grep 'keyword' file name")    
    else:    
        search=open(file, 'r').read().find(keyword)
        if search is -1:
            print("keyword not found")
          
        else:
            fout=open("temp.txt","w")                     
            print "keyword word found"
            if os.stat("/root/mail.txt").st_size == 0:  #if size of file is zero don't print
                with open(file) as origin:
                    for line in origin:
                        if keyword in line:
                            print line.replace(keyword,Fore.RED+keyword+Fore.RESET)
                        line=line.rstrip()
            with open(file) as origin:
                for line in origin:
                    if keyword in line:
                        fout.write(line.replace(keyword,Fore.RED+keyword+Fore.RESET))
                    line=line.rstrip()
            fout.close()
            
    return;
