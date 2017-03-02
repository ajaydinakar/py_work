#!/usr/bin/env python
import os
def cat(file1,file2):
    if file1 is None and file2 is None:   
        print("you didnt given the file name or file doest exists")
    if file1 is 'one':                    #if one indicate to display one file
        fout=open("temp.txt ","w")
    
        fin = open(file2, "r")
        read=fin.read()
        fout.write(read)
        #fout.write('\n')        
        fin.close()
        fout.close()
        fout=open("temp.txt ","r")
        if os.stat("/root/mail.txt").st_size == 0:
            print fout.read()
        fout.close()
    else:
        fout=open("temp.txt ","w")     #else there are two files ,concat them and display
        fin = open(file1, 'r')
        read=fin.read()
        fout.write(read)
        
        #fout.write('\n')                     
        fin.close()
        fin = open(file2, 'r')
        read=fin.read()
        fout.write(read)
        fin.close()
        fout.close()
        fout=open("temp.txt ","r")
        if os.stat("/root/mail.txt").st_size == 0:
            print fout.read()
        fout.close()
   
            
    return;
