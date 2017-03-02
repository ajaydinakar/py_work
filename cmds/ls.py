
#!/usr/bin/env python
"""@main module Name:ls,
other functions :color for colour display
                 HR for converting size to human redable
                 octal_convert for converting stat.ST_mode to string
refences:http://python-reference.readthedocs.io/en/latest/docs/str/ljust.html
               https://www.youtube.com/watch?v=TvOKST5A6kI -for colors
                https://www.tutorialspoint.com/python/os_stat.htm
"""
import os
import time
import pwd
import grp
import stat
from colorama import *

def color(f):
    if os.path.isdir(f) == True:
        return Fore.BLUE+f+Fore.RESET+'/'
    if f.startswith('.'):
        return Fore.GREEN+f+Fore.RESET
    else:
        return f
def colum(f):#not used
    colum=6
    for count, item in enumerate(sorted(f), 1):
        if os.path.isdir(item) == True:
            print Fore.BLUE+item.ljust(20)+Fore.RESET,  # make each colum for 20 space
        else:
            print  item.ljust(20),
        if count % colum == 0:
            print

def HR(size,precision=2):
    size=int(size)
    suffixes=[' ','KB','MB','GB','TB']
    suffixIndex = 0
    while size > 1024:
        suffixIndex += 1 #increment the index of the suffix
        size = size/1024.0 #apply the division
    return " %d%s"%(size,suffixes[suffixIndex])
#octal conversion ref :https://github.com/viorels/ls/blob/master/ls.py#L75
def octal_convert(mode):
    octal = oct(mode)[-3:]
    perms = ''
    for octdigit in octal:
        intdigit = int(octdigit)
        perms += 'r' if intdigit & 4 else '-'
        perms += 'w' if intdigit & 2 else '-'
        perms += 'x' if intdigit & 1 else '-'
    
    if (mode==16877):
        perms='d'+perms
    else:
        perms='-'+perms
    return perms
import pwd
def ls(flag=None):
    if flag is None:
        list =os.listdir('.')
        list =filter(lambda f: not f.startswith('.'), list)
        out=open("temp.txt","w")
        colum=6
        for count, item in enumerate(sorted(list), 1):
            if os.path.isdir(item) == True: 
                item=item+'/'
                out.write( Fore.BLUE+item.ljust(20)+Fore.RESET,)
            else:
                out.write(  item.ljust(20),)
            if count % colum == 0:
                out.write("\n")
        out.close()
        out=open("temp.txt","r")
        if os.stat("/root/mail.txt").st_size == 0:
            print out.read()
        out.close()
    elif flag=='-l':
        out=open("temp.txt","w+")
        list=filter( lambda f: not f.startswith('.'), os.listdir(os.getcwd()))
        list.sort()
        for f in list:
            
            out.write('%-12s%-4s%-8s%-8s%-10s%-18s%-12s' %(octal_convert(os.stat(f).st_mode),os.stat(f).st_nlink,grp.getgrgid(os.stat(f).st_gid).gr_name,grp.getgrgid(os.stat(f).st_gid).gr_name ,os.stat(f).st_size ,time.strftime('%b %d %Y %H:%M',time.localtime(os.stat(f).st_mtime)),color(f)))
            out.write('\n')
        out.close()
        out=open("temp.txt","r")
        if os.stat("/root/mail.txt").st_size == 0:
            print out.read()
            #print pwd.getpwuid(os.getuid()).pw_name
        out.close()
    elif flag=='-a':
        list =os.listdir(os.getcwd())
        list=['.','..']+list
        out=open("temp.txt","w")
        colum=6
        for count, item in enumerate(sorted(list), 1):
            if os.path.isdir(item) == True:
                out.write( Fore.BLUE+item.ljust(20)+Fore.RESET,)
            elif item.startswith('.'):
                out.write(Fore.GREEN+item.ljust(20)+Fore.RESET,)
            else:
                out.write(  item.ljust(20),)
            if count % colum == 0:
                out.write("\n")
        out.close()
        out=open("temp.txt","r")
        if os.stat("/root/mail.txt").st_size == 0:
            print out.read()
        out.close()
    elif flag=='-la':
        out=open("temp.txt","w+")
        list=os.listdir(os.getcwd())
        list=['.','..']+list
        list.sort()
        for f in list:

            out.write('%-12s%-4s%-8s%-8s%-10s%-18s%-12s' %(octal_convert(os.stat(f).st_mode),os.stat(f).st_nlink,grp.getgrgid(os.stat(f).st_gid).gr_name,grp.getgrgid(os.stat(f).st_gid).gr_name ,os.stat(f).st_size ,time.strftime('%b %d %Y %H:%M',time.localtime(os.stat(f).st_mtime)),color(f)))
            out.write('\n')
        out.close()
        out=open("temp.txt","r")
        if os.stat("/root/mail.txt").st_size == 0:
            print out.read()
            #print pwd.getpwuid(os.getuid()).pw_name
        out.close()

    elif flag=='-lh':
        out=open("temp.txt","w+")
        list=os.listdir(os.getcwd())
        list=filter( lambda f: not f.startswith('.'), os.listdir(os.getcwd()))
        list.sort()
        for f in list:
              #all the info of file/dir stus from os.stat
            out.write('%-12s%-4s%-8s%-8s%-10s%-18s%-12s' %(octal_convert(os.stat(f).st_mode),os.stat(f).st_nlink,grp.getgrgid(os.stat(f).st_gid).gr_name,grp.getgrgid(os.stat(f).st_gid).gr_name ,HR(os.stat(f).st_size) ,time.strftime('%b %d %Y %H:%M',time.localtime(os.stat(f).st_mtime)),color(f)))
            out.write('\n')
        out.close()
        out=open("temp.txt","r")
        if os.stat("/root/mail.txt").st_size == 0:
            print out.read()
            #print pwd.getpwuid(os.getuid()).pw_name
        out.close()
   
    elif flag=='-lah':
        out=open("temp.txt","w+")
        list=os.listdir(os.getcwd())
        list=['.','..']+list
        list.sort()
        for f in list:
              #all the info of file/dir stus from os.stat
            out.write('%-12s%-4s%-8s%-8s%-10s%-18s%-12s' %(octal_convert(os.stat(f).st_mode),os.stat(f).st_nlink,grp.getgrgid(os.stat(f).st_gid).gr_name,grp.getgrgid(os.stat(f).st_gid).gr_name ,HR(os.stat(f).st_size) ,time.strftime('%b %d %Y %H:%M',time.localtime(os.stat(f).st_mtime)),color(f)))
            out.write('\n')
        out.close()
        out=open("temp.txt","r")
        if os.stat("/root/mail.txt").st_size == 0:
            print out.read()
            #print pwd.getpwuid(os.getuid()).pw_name
        out.close()

    else:
        print("give flag -l or -a or -h")
    return;


