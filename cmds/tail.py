
#!/usr/bin/env python
import os
def tail(file):
    if file is None:
        print("enter a file name to display")
    with open(file,'r') as myfile:
        line=(myfile.readlines()[-10:])
    fout=open("temp.txt","w")

    for i in range(10):
        line[i]=line[i].strip()
        fout.write(line[i])
        fout.write('\n')
    fout.close()
    if os.stat("/root/mail.txt").st_size == 0:    
        f=open("temp.txt","r")
        print f.read()   
        f.close()    
    return;

