#!/usr/bin/env python

import sys
f = open(sys.argv[1])

#f = open("fly.sam")

counter = 0

for line in f.readlines():
    line = line.rstrip("\r\n")
    if line.startswith("SRR"): 
        counter += 1
print counter



