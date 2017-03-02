#!/usr/bin/env python
#Function name hiscmd
# finds the commands assosiated with a number starts with !. ex:!451
import os
def hiscmd(num):

    i=1
    num=num.replace('!',"")
    num=int(num) 
    fin=open('/root/history.txt', 'r')
    for line in fin:   #finding the number of the assosiated command
        if num==i:        
            print i,line
            os.system(line)  # execute
        i=1+i

  
    return;
    

