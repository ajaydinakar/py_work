#!/usr/bin/env python
import os
"""list =os.listdir(os.getcwd()) 
length =len(list)
ls=''
for i in range(length):
    ls=ls+list[i]+" "
print(ls)
f=open('/root/md.txt','w')
f.truncate()
f.write(ls)
f.truncate()

""
var=raw_input()
if var.find('|'):
    var=var.split('|')
print var
"""

input=raw_input("%")

if input.find('|'):
    input=input.split(" | ")
var1= input[0]
var2= input[1]
   # one_cmd(var[0])
var2=var2+" "+"md.txt"
  #  one_cmd(var2)

print var2
