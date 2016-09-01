#!/usr/bin/env python
import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy

df = pd.read_csv(sys.argv[1], sep="\t")
df2 = pd.read_csv(sys.argv[2], sep="\t")


df_roi = df["gene_name"] == "Sxl"
df_name = df[df_roi]
#print df_name["gene_name"]
df_roi2 = df_name["FPKM"] > 0
df_FPKM = df_name[df_roi2]
#print df_FPKM
fpkm_values = numpy.log(df_FPKM["FPKM"])
print fpkm_values

df_roi3 = df2["gene_name"] == "Sxl"
df_name3 = df2[df_roi]
#print df_name3["gene_name"]
df_roi4 = df_name3["FPKM"] > 0
df_FPKM2 = df_name3[df_roi2]
#print df_FPKM2
fpkm_values2 = numpy.log(df_FPKM2["FPKM"])
print fpkm_values2
# df_overlap = pd.merge(df_FPKM, df_FPKM2, on="gene_name")
# print df_overlap

plt.figure()

plt.boxplot( [fpkm_values, fpkm_values2], labels = ["SRR1", "SRR2"] )
plt.title("SRR Wut")

plt.ylabel("log(FPKM)")
plt.savefig("boxplot.png")

plt.close()




