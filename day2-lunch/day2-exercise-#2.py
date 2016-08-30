#!/usr/bin/env python

import sys
f = open(sys.argv[1])

count = 0

for line in f.readlines():
    line = line.rstrip("\r\n")
    if "XM:i:0" in line:
        count += 1
print count