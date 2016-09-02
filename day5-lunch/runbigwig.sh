#!/bin/bash


./day5-lunch.py ~/data/results/stringtie/SRR072893/t_data.ctab
for i in *.bw
do
	bigWigAverageOverBed -bedOut=${i%bw}bed $i prom.bed ${i%bw}tab
done

./linreg.py *3.bed
