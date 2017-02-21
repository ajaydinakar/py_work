import os
def rm(arg=None):
    cmd="rm"
    if arg is None:
        print("err :must enter the file name after rm command ")

    else:
        os.remove(arg)
    return;
