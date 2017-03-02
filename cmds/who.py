#!/usr/bin/env python
import os 
import pwd
def who():
    #userhome = os.getusername()
    #print(userhome)
    #print(pwd.getpwuid( os.getuid() ))
    print (os.getlogin())
    return;


