"""

This is the main data readin and transform file to prepare the dataset for model.py

Author: Jamie Chen

"""

import pandas as pd
import logging

# create logging file
logging.basicConfig(filename='data_preprocess.log',level=logging.DEBUG)

def preprocess(datafolder,filename):
	""" Preprocessing: load the data and clean/transform

	:param datafolder: Folder name of input data file
    :param filename: Input filename

	"""
	inpath = datafolder
	infilename = filename
	infile = pd.read_csv(inpath + "/" +infilename)
	logging.debug('File read in from %s', inpath)

	#coerce categorical variables to category type
	categoryVariableList = ["hr","weekday","mnth","season","weathersit","holiday","workingday"]
	for var in categoryVariableList:
		infile[var] = infile[var].astype("category")
	logging.info('Set categorical variables to data type "category"')

	#drop insignificant/redundant features
	infile = infile.drop(['instant'], axis=1)
	dropFeatures = ["casual","atemp", "season","registered", "dteday", "dayofmonth", "workingday", "yr", "holiday"]
	final_data = infile.drop(dropFeatures, axis =1)
	logging.info('Dropped trivial features based on EDA finding"')

	return final_data

hour = preprocess("data","hour.csv")

print(" Data has been read in and preprocessed for model building.")
