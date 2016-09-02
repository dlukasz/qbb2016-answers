#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from sklearn import datasets
import numpy as np

df = pd.read_csv(sys.argv[1], sep="\t")
#df = pd.read_table(sys.argv[1])


df_roi = df["FPKM"] > 0
df_FPKM = df[df_roi]
fpkm_values = np.log10(df_FPKM["FPKM"])
print fpkm_values
#mean = fpkm_values.mean()
#print mean

plt.figure()
plt.hist(fpkm_values, bins = 100)
plt.title("FPKM values for SRR072893")
plt.xlabel("FPKM value")
plt.ylabel("Number of occurrences")
plt.savefig("histogram.png")

plt.close()