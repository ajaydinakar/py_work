
#!/usr/bin/env python
import os
def hd(file):
    if file is None:
        print("enter a file name to display")
        return
    fout=open("temp.txt","w")
    with open(file,'r') as myfile:
        line=((myfile.readlines()[:11]))
    fout=open("temp.txt","w")

    for i in range(10):
        line[i]=line[i].rstrip()
        fout.write(line[i])
        fout.write('\n')
    fout.close()
    if os.stat("/root/mail.txt").st_size == 0:
        f=open("temp.txt","r")
        print f.read()
        f.close()
    return;

