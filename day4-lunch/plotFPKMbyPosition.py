#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_table(sys.argv[1])
df2 = pd.read_table(sys.argv[2])
window_size = sys.argv[3]

chrom = ["2L", "2R", "3L", "3R", "4", "X"]
files = [df, df2]

def roll_plot(chrom):
    output_list = []
    for item in files:
        df_roi = item["chr"] == chrom
        df_chrom = item[df_roi]
        smoothed = df_chrom["FPKM"].rolling( int(window_size) ).mean()
        output_list.append(smoothed)
    plt.figure()
    plt.plot(output_list[0])
    plt.plot(output_list[1])
    plt.title("Rolling mean (size = " + window_size + ") for " + chrom)
    plt.savefig(chrom + "_plot.png")
    plt.close()

for item in chrom:
    roll_plot(item) 
   