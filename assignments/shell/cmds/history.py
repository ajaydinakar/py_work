#!/usr/bin/env python

def history():

    i=1
    fin=open('/root/.bash_history', 'r')
    for line in fin:
        print i,line
        i=1+i

  
    return;


