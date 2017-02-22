"""This Function counts the number of lines,words,characters in a file
"""
#!/usr/bin/env python

def wc(file):
    chars = words = lines = 0
    with open(file, 'r') as in_file:
        for line in in_file:
            lines += 1
            words += len(line.split())
            chars += len(line)
    print(lines,  words  , chars)


    return;


