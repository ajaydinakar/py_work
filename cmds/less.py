
#!/usr/bin/env python
#Function name less
#displays file as like pages
from colorama import *
import os
def less(file):
    if file is None:
        print "give file name"
    else:
        i=j=0

        f=open(file,'r')
        lines =len(f.readlines())
        f.close()
        f=open(file,'r')
        fout=open("temp.txt","w")
        if os.stat("/root/mail.txt").st_size == 0:
            for line in range(lines):
                i=i+1
                display= f.readline()
                display=display.rstrip()
                print display
                if(i==65):
                    print Back.WHITE+Fore.BLACK+"Press Enter"+Fore.RESET+Back.RESET+"                                            "+Back.WHITE+Fore.BLACK+"Page"+str(j)+Fore.RESET+Back.RESET
                    raw_input()
                    i=0
                    j=j+1
            print Back.WHITE+Fore.BLACK+"  END  "+Fore.RESET+Back.RESET
        f.seek(0)
        read=f.read()
        fout.write(read)
        fout.close()    
        f.close()

