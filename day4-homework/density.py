#!/usr/bin/env python

import sys
import pandas as pd

from sklearn import datasets
import numpy as np


import matplotlib.pyplot as plt

from scipy.stats import gaussian_kde


data = pd.read_csv(sys.argv[1], sep="\t")
df_raw = data["FPKM"] + 1
#df_raw2 = df_raw["FPKM"]
df_log = np.log10(df_raw)



density = gaussian_kde(df_log)

# xs = np.linspace(0,8,200)
# density.covariance_factor = lambda : .25
# density._compute_covariance()
# plt.plot(xs,density(xs))
xs = np.linspace(-5, 5, 200)
#start, stop, resolution(number of points between those two numbers so it adds points along the x axis)

plt.figure()
plt.plot(xs, density(xs))
plt.title("Density Plot")
plt.xlabel("FPKM values")
plt.ylabel("Density")
plt.savefig("density.png")
plt.close()