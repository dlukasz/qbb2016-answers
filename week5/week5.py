df <- read.delim("~/qbb2016-answers/week5/genodata.out.eigenvec", header=F, sep = " ")
plot(df$V3,df$V4,)

df2 <- read.delim("~/qbb2016-answers/week5/alleles.txt", header =T, sep = "\t")
hist(df2$MAF, breaks = 100, col = "green")

awk '{print $1"\t"$2"\t"$3"\t"$4"\t"$5"\t"$6"\t"}' plink.frq > alleles.txt
plink2 --freq --vcf genodata.vcf.gz 

R plot for Manhattan plots (x46 phenotypes)

file = list.files("~/qbb2016-answers/complab/week4/", pattern = ".*qassoc", full.names = T)

for (i in file)\{\
  df3 <- read.delim(i, header = T )\
  name = gsub("/Users/cmdb/qbb2016-answers/complab/week4//plink.", "", i)\
  name = gsub(".qassoc", "", name)\
  for (j in 1:nrow(df3))\{\
    if (df3[j,9] < .00001) \{df3[j, 10]= "red"\}\
    else \{df3[j, 10]="black"\}\
  \}\
  newname = gsub("qassoc", "png", i)\
  par(mar=c(5,5,2,2))\
  png(newname, width = 6, height = 3.5, units = "in", res = 120, pointsize = 5)\
  plot(rownames(df3), -log(df3$P), col = adjustcolor(df3$V10, alpha = .2), pch = 10, xaxt = "n", xlab= "chromosome", ylab = "-logP", main = paste("GWAS", name))\
  axis(1, c(1, 209, 1112, 1280, 2546, 3109, 3444, 4538, 4980,5526,6383,7220, 8432, 9273, 9907, 10999), c("1", "2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"), cex.axis = 0.75)\
  abline(a = -log(0.00001), b = 0, lwd = 6, lty = 2, col = "blue")\
  dev.off()\
\}}
