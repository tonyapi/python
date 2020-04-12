# -problem3_6.py *- coding: utf-8 -*-

import sys

infile = sys.argv[1]
outfile = sys.argv[2]
    
f = open(infile)
h = open(outfile, 'w') 
for line in f:
    newline = line.strip("\n")
    lenght = str(len(newline))
    print(lenght)
    h.write(lenght)
    h.write("\n")

f.close()
h.close()
