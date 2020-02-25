# project_level_VCF
Merges VCFs which have genotype data into a matrix. Creates a project level VCF which is a matrix and has these values:
0 : Reference
1 : Heterozygous
2 : Homozygous

This matrix can be loaded in R and parsed but please replace the ","  with "\t".

Use a standard VCF which has genotype information. The input file example is in the example directory.

It should have these fields:
CHROM
POS
ID
REF
ALT
QUAL
FILTER
INFO
FORMAT
"Sample info with genotype represented in FORMAT"
This does not work on multiallelic sites.
It has been tested on 10 VCF files and runs just fine.
