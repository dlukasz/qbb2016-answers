#!/usr/bin/env python

import sys
f = open(sys.argv[1])

counter = 0

for line in f.readlines():
    if line.startswith("SRR"):
        print (line.split("\t")[2])
        counter += 1
        if counter == 10:
            break
    