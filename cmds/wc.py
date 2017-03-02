"""This Function counts the number of lines,words,characters in a file
   
"""
#!/usr/bin/env python
import os 
def wc(flag=None,file=None):
   
    if flag is 'one':#flag one the there is no flag
  
        chars = words = lines = 0
        with open(file, 'r') as in_file:
            for line in in_file:
                lines += 1
                words += len(line.split())
                chars += len(line)
        out=open("temp.txt","w")
        out.write(str(lines))
        out.write('\t')
        out.write(str(words))
	out.write('\t')
        out.write(str(chars))
        out.close()
        out=open("temp.txt","r")
        if os.stat("/root/mail.txt").st_size == 0:
            print out.read()
        out.close()
    if flag == '-l':   #for lines
        lines = 0
        with open(file, 'r') as in_file:
            for line in in_file:
                lines += 1
        out=open("temp.txt","w")
        out.write(str(lines))
        out.close()
        out=open("temp.txt","r")
        if os.stat("/root/mail.txt").st_size == 0:
            print out.read()
        out.close()
    if flag == '-w':       #for words
        lines = words =0
        with open(file, 'r') as in_file:
            for line in in_file:
                lines += 1
                words += len(line.split())
        out=open("temp.txt","w")
        out.write(str(words))
        out.close()
        out=open("temp.txt","r")
        if os.stat("/root/mail.txt").st_size == 0:
            print out.read()
        out.close()
    if flag == '-c':        #for characters
        lines = words = chars = 0
        with open(file, 'r') as in_file:
            for line in in_file:
                lines += 1
                words += len(line.split())
                chars += len(line)

        out=open("temp.txt","w")
        out.write(str(chars))
        out.close()
        out=open("temp.txt","r")
        if os.stat("/root/mail.txt").st_size == 0:
            print out.read()
        out.close()


    return;


