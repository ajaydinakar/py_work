#!/usr/bin/env python
import os
def history():

    if os.stat("/root/mail.txt").st_size == 0:
        i=1
        fin=open('/root/history.txt', 'r')
        fout=open('temp.txt',"w")
        for line in fin:
            line=line.rstrip()
            fout.write(str(i))
            fout.write('\t')
            fout.write( line)
            fout.write('\n')
            i=1+i
        fout.close()
        fout=open('temp.txt',"r")
        print fout.read()
    else:
        i=1
        fin=open('/root/history.txt', 'r')
        fout=open('temp.txt',"w")
        for line in fin:
            line=line.rstrip()
            fout.write(str(i))
            fout.write('\t')
            fout.write( line)
            fout.write('\n')
            i=1+i
        fout.close()
 
    return;


