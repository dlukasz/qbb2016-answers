#!/usr/bin/env python

import fastar2
import sys
import numpy as np


contigs = fastar2.FASTAReader(open(sys.argv[1]))

contig_number = 0
max_length = 0
total_contig = 0
lengths = []

for ident, seq in contigs:
    contig_number += 1
#print contig_number
    #if len(seq) > max_length:
     #   max_length = len(seq)
    lengths.append(len(seq))
    total_contig += len(seq)
    
print min(lengths)
print max(lengths)
print np.median(lengths)
    #print max_length
#min_length = 100000
#for ident, seq in contigs:
 #   if len(seq) < min_length:
  #      min_length = len(seq)
#print max_length
   # print min_length
    #total_contig += len(seq)
print total_contig/contig_number
    
#print numpy.median(lengths)

# outputs for velvet:
# 61
# 998
# 126.0
# 186

# outputs for spades (did not use the --only-assembler option)
# 207
# 1737
# 335.0
# 389