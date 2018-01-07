import os
import time
import pwd
import grp


def get_perms_text(mode):
    octal = oct(mode)[-3:]
    perms = ''
    for octdigit in octal:
        intdigit = int(octdigit)
        perms += 'r' if intdigit & 4 else '-'
        perms += 'w' if intdigit & 2 else '-'
        perms += 'x' if intdigit & 1 else '-'
    return perms





for f in os.listdir(os.getcwd()):
    print '%-12s%-4s%-8s%-8s%-10s%-18s%-12s' %((os.stat(f).st_mode),os.stat(f).st_nlink,pwd.getpwuid(os.stat(f).st_uid).pw_name, grp.getgrgid(os.stat(f).st_gid).gr_name ,os.stat(f).st_size ,time.strftime('%b %d %Y %H:%M',time.localtime(os.stat(f).st_mtime)),f) 
#    print os.stat(f)  
#time.strftime('%b %d %Y %H:%M', time.localtime(stat.st_mtime))

