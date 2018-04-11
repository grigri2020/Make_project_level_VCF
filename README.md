# project_level_VCF
Merges VCFs which have genotype data into a matrix. Creates a project level VCF which is a matrix and has these values:
0 : Reference
1 : Heterozygous
2 : Homozygous

This matrix can be loaded in R and parsed but please replace the ","  with "\t".

Use a standard VCF which has genotype information. The input file should roughly look like this 
================================== INPUT VCF FILE FORMAT =========================================================

##INFO=<ID=ENN,Number=1,Type=String,Description="Encode Name">
##INFO=<ID=ENC,Number=1,Type=String,Description="Encode class">
#CHROM  POS     ID      REF     ALT     QUAL    FILTER  INFO    FORMAT  1013_realigned_2.txt.dedup.recaled
1       14610   .       T       C       2       low_snpqual     AC=0;AF=0.000000;ReqIncl=.;PU=.;RFG=ncRNA_exonic;GI=WASH7P,NONE(dist=NONE),NONE(dist=NONE),ENSG00000227232;UCG=ncRNA_exonic;ENS=ncRNA_exonic;ENSGN=ENSG00000227232;MT=intergenic;MTGN=.;GN=WASH7P;RSID=.;CD=.;HT=.;HC=.;HD=.;HP=.;AV=.;AT=.;EV=.;ET=.;CG=.;IET=0;IEO=0;IEN=.;MS=0.2;TMAF=.;TAMR=.;TASN=.;TAFR=.;TEUR=.;SF=.;SD=.;SM=.;SX=.;CID=.;CGENE=.;CSTRAND=.;CCDS=.;CAA=.;CCNT=.;NA=.;NC=.;NE=.;NF=.;NG=.;NH=.;NI=.;NJ=.;NK=.;NL=.;NM=.;ENN=H3K36me3,H3K27me3;ENC=Histone GT:VR:RR:DP:GQ  0/1:3:4:7:.
1       14653   .       C       T       60      single_strand   AC=0;AF=0.000000;ReqIncl=.;PU=.;RFG=ncRNA_exonic;GI=WASH7P,NONE(dist=NONE),NONE(dist=NONE),ENSG00000227232;UCG=ncRNA_exonic;ENS=ncRNA_exonic;ENSGN=ENSG00000227232;MT=intergenic;MTGN=.;GN=WASH7P;RSID=rs375086259;CD=.;HT=.;HC=.;HD=.;HP=.;AV=.;AT=.;EV=.;ET=.;CG=.;IET=0;IEO=0;IEN=.;MS=0.25;TMAF=.;TAMR=.;TASN=.;TAFR=.;TEUR=.;SF=.;SD=.;SM=.;SX=.;CID=.;CGENE=.;CSTRAND=.;CCDS=.;CAA=.;CCNT=.;NA=.;NC=.;NE=.;NF=.;NG=.;NH=.;NI=.;NJ=.;NK=.;NL=.;NM=.;ENN=H3K36me3,H3K27me3;ENC=Histone      GT:VR:RR:DP:GQ  0/1:16:15:31:.

=======================================================================================================================
In short, it should have these fields:
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
