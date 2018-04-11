#Create a matrix from 
import numpy as np
import pandas as pd
import os, sys
import getopt


#Just creates an empty dictionary to store all the info in the 
#vcf files
def create_empty_dict():
	d = dict()
	return d


#Creates the header from the VCF file (standard)
def create_vcf_header(arg_list):
	VCF_HEADER = ['CHROM','POS','ID','REF','ALT','QUAL','FILTER','INFO','FORMAT']
	for a in arg_list:
		VCF_HEADER.append(a)
	return VCF_HEADER


#Define which genotype to the appropriate one.
# Does not work for multiallelic sites
def genotype_snp( snp ):
	if(snp == '0/0'):
		return '0'
	elif(snp == '0/1'):
		return '1'
	elif(snp == '1/1'):
		return '2'
	elif(snp == './.'):
		return '.'
	else:
		pass


#Get options. This should be using getopt but did not have time!
def get_options():
	if 


#Checks if key exists in the dictionary, if not => insert! 
def insert_dict(dictionary, key_ele, val_ele):
	if key_ele in dictionary:
        	dictionary[key_ele].append(val_ele)
        else:
                dictionary[key_ele] = [val_ele]

#Hello Main! 
def main():
	arg_list = get_options()
	dictionary, drows = read_vcf(arg_list)
	print_dataframe(drows, dictionary, arg_list)


#Finally print the dataframe. What a relief! 
def print_dataframe(nrows,d, arg_list ):
	pd.set_option('display.max_rows', nrows)	
	df = pd.DataFrame.from_dict(d, orient='index')
	df.columns = arg_list
	df.fillna(value='NA', inplace=True)
	df.sort_index(axis=0).to_csv(path_or_buf='output', sep=',',header=True, index=True)


#Reads the VCF file, parses it and extracts the genotype for each SNP
def read_vcf(arg_list):

	display_opts = 0
	d = create_empty_dict()
	VCF_HEADER = create_vcf_header(arg_list)

	count_args = 0
	 
	for vcf_file in arg_list:
		vcf = pd.read_csv(vcf_file, sep='\t', header=None, comment='#', names=VCF_HEADER, low_memory=False)
		display_opts = display_opts + vcf.shape[0]
		#print vcf
		
		gen_vcf_split = pd.DataFrame([ x.split(':') for x in vcf[arg_list[count_args]].tolist()], columns=['GT','VR','RR','DP','GQ'])
		count = 0 
		for j in gen_vcf_split['GT']:
			pos = str(vcf['CHROM'].iloc[count]) + ":" + str(vcf['POS'].iloc[count])
			ret_gen = genotype_snp(j)
			count =  count + 1 
			insert_dict(d, pos, ret_gen)

	return (d, display_opts)
	

#Customer support options
def usage():
	print "This is now how its done. Please input at least 1 VCF file\n"


#This is where it all began
if __name__ == "__main__": main()
