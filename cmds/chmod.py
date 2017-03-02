#!/usr/bin/env python
import os
def chmod(mode,path):
    mode=int(mode)
    os.chmod(path,mode)
    return;


