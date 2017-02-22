
#!/usr/bin/env python

def tail(file):
    if file is None:
        print("enter a file name to display")
    with open(file,'r') as myfile:
        line=(myfile.readlines()[-7:])
    for i in range(6):
        print(line[i])
    return;

