"""

This is the main data readin and transform file to prepare the dataset for model.py

Author: Jamie Chen

"""

import pandas as pd


def preprocess(datafolder,filename):
	""" Preprocessing

	Readin:
	load the data from the folder in the same directory and save as a pd dataframe

	Data transform:
	1. Coerce categorical variables to be of type category
	2. drop row identifier and features based on EDA

	"""
	inpath = datafolder
	infilename = filename
	infile = pd.read_csv(inpath + "/" +infilename)

	#coerce categorical variables to category type
	categoryVariableList = ["hr","weekday","mnth","season","weathersit","holiday","workingday"]
	for var in categoryVariableList:
		infile[var] = infile[var].astype("category")

	#drop insignificant/redundant features
	infile = infile.drop(['instant'], axis=1)
	dropFeatures = ["casual","atemp", "season","registered", "dteday", "dayofmonth", "workingday", "yr", "holiday"]
	final_data = infile.drop(dropFeatures, axis =1)
	return final_data

hour = preprocess("data","hour.csv")

print(" Data has been read in and preprocessed for model building.")
