#!/usr/bin/env python


def hiscmd(num):

    i=1
    num=num.replace('!',"")
    num=int(num) 
    fin=open('/root/.bash_history', 'r')
    for line in fin:
        if num==i:        
            print i,line
        i=1+i

  
    return;
    

