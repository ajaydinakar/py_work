#!/usr/bin/env python

import shutil
from shutil import copyfile


def cp(src=None,dst=None):
    if src is None or dst is None:
        print("err: must enter the sourse and destination names to copy")
    else:
        copyfile(src,dst)
    return;
