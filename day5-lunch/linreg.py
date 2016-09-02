#!/usr/bin/env python

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#import pyBigWig as bw
import statsmodels.api as smf

files = sys.argv[1:]

for i in files:
    df = pd.read_table(i, header=None)
    fpkm = df[4]
    chip_mean = df[5]
    model = smf.OLS(chip_mean, fpkm)
    results = model.fit()
    print results.summary()

     
