#!/usr/bin/env python
import os
def mkdir(arg=None):
    if arg is None:
        print("err :must enter the file name after less command ")
    else:
        os.mkdir(arg)
    return;
