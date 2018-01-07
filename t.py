#!/usr/bin/env python
import os

 if file is None:
        print("enter a file name to display")
    fout=open("temp.txt","w")
    with open(file,'r') as myfile:
        line=str((myfile.readlines()[:10]))
        with open(filename) as f_in:
            lines = filter(None, (line.rstrip() for line in f_in))
        fout.write(line)
        fout.write('\n')
    fout.close()
    fout=open("temp.txt","r")
    print fout.read()
    fout.close()
    return;








fin=open('twin.txt', 'r')
        fout=open('temp.txt',"w")
        for line in fin:
            line=line.rstrip()
            fout.write( line)
            fout.write('\n')
            i=1+i
        fout.close()

