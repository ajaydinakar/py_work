import os
import pwd

#num="!256"
#if '!' in num:
 #   num=num.replace("!","0")
  #  print num    
print pwd.getpwuid(os.getuid()).pw_gecos

