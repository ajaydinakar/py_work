#!/usr/bin/env python
import shutil

def mv(src=None,dst=None):
    if src is None or dst is None:
        print("err: must enter the sourse and destination names to copy")
    else:
        shutil.move(src,dst)
    return;
