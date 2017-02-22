#!/usr/bin/env python
import shutil
def rmdir(arg=None):
    if arg is None:
        print("err :must enter a directory name after mkdir command ")
    else:
        shutil.rmtree(arg)
    return;
