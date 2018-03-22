"""

This is the main random forest model file for predicting bikeshare demand.

Author: Jamie Chen

"""

import data
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import pickle
from sklearn.externals import joblib

import logging

def rfmodel(hour):
	""" Train a random forest model
	split dataset into test and train and run rf regression
	
	:param hour: input pandas dataframe
	
	"""

	#split data into test and train
	datatrain = hour[hour["train"] == 1]
	datatest = hour[hour["train"]!=1]
	logging.info('Split data into test and train.')

	#log transform reponse variable "cnt" - bike count
	y = datatrain["cnt"]
	ylabelslog = np.log1p(y)
	X=datatrain.drop(["cnt", "train"], 1)
	logging.info('Applied log transformation to response variable bike count.')

	#train random forest model
	rfmodel = RandomForestRegressor(n_estimators=100)
	rfmodel.fit(X, ylabelslog)
	logging.info('Trained a random forest model.')

	#create pickle file
	model_name = 'rf.pkl'
	model_pkl = open(model_name, 'wb')
	pickle.dump(rfmodel, model_pkl)
	model_pkl.close()
	logging.info('Saved model in a pkl file.')

if __name__ == "__main__":
	rfmodel(data.preprocess("data","hour.csv"))
