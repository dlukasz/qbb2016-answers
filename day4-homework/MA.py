#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from sklearn import datasets
import numpy as np

df1 = pd.read_csv(sys.argv[1], sep="\t")
df2 = pd.read_csv(sys.argv[2], sep="\t")

df1_log = np.log2(df1["FPKM"] + 1)
df2_log = np.log2(df2["FPKM"] + 1)

fold_change = df1_log - df2_log
mean_expression = (df1_log + df2_log)/2

plt.figure()
plt.scatter(mean_expression, fold_change, alpha=0.1)
plt.title("MA Plot")
plt.xlabel("mean expression")
plt.ylabel("fold change")
plt.savefig("MA_plot.png")

plt.close()
