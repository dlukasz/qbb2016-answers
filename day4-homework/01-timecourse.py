#!/usr/bin/env python

"""
Usage: ./01-timecourse.py <metadata.csv> <ctab_dir>
    e.g. ./01-timecourse.py samples.csv ~/data/results/stringtie
"""

import sys
import pandas as pd
import matplotlib.pyplot as plt

df_meta = pd.read_csv(sys.argv[1])
df_meta2 = pd.read_csv(sys.argv[2])
ctab_dir = sys.argv[3]


fem_Sxl = []

dr_roi = df_meta[ "sex" ] == "female"
for sample in df_meta [ dr_roi ]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table( filename )
    
    df_roi2 = df[ "t_name"] == "FBtr0331261"
    fem_Sxl.append(df[ df_roi2 ]["FPKM"].values)
    
male_Sxl = []

dr_roi3 = df_meta[ "sex" ] == "male"
for sample in df_meta [ dr_roi3 ]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table( filename )
    
    df_roi3 = df[ "t_name"] == "FBtr0331261"
    male_Sxl.append(df[ df_roi3 ]["FPKM"].values)
    
male_rep_Sxl = []

dr_roi4 = df_meta2[ "sex" ] == "male"
for sample in df_meta2 [ dr_roi4 ]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table( filename )
    
    df_roi4 = df[ "t_name"] == "FBtr0331261"
    male_rep_Sxl.append(df[ df_roi4 ]["FPKM"].values)

fem_rep_Sxl = []

dr_roi5 = df_meta2[ "sex" ] == "female"
for sample in df_meta2 [ dr_roi5 ]["sample"]:
    filename = ctab_dir + "/" + sample + "/t_data.ctab"
    df = pd.read_table( filename )
    
    df_roi5 = df[ "t_name"] == "FBtr0331261"
    fem_rep_Sxl.append(df[ df_roi5 ]["FPKM"].values)


# [ 1, 0, 2, 10, 50, 100]

plt.figure()
plt.plot(fem_Sxl,'r-')
plt.plot(male_Sxl,'b-')
plt.plot([4, 5, 6, 7], male_rep_Sxl,'go')
plt.plot([4, 5, 6, 7], fem_rep_Sxl, 'ro')
plt.legend(["Females", "Males", "Males-Replicates", "Females-Replicates"], loc="upper left")
plt.xticks(range(0, 8), ["10", "11", "12", "13", "14A", "14B", "14C", "14D"])
#plt.show()
plt.title("Sxl")
plt.xlabel("developmental stage")
plt.ylabel("mRNA abundance (RPKM)")
plt.savefig("timecourse.png")
plt.close()

