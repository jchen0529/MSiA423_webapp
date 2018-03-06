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

def rfmodel(hour):
	""" Main random forest function
	split dataset into test and train and run rf regression

	"""

	#split data into test and train
	datatrain = hour[hour["train"] == 1]
	datatest = hour[hour["train"]!=1]

	#log transform reponse variable "cnt" - bike count
	y = datatrain["cnt"]
	ylabelslog = np.log1p(y)
	X=datatrain.drop(["cnt", "train"], 1)

	#train random forest model
	rfmodel = RandomForestRegressor(n_estimators=100)
	rfmodel.fit(X, ylabelslog)

	#create pickle file
	model_name = 'rf.pkl'
	model_pkl = open(model_name, 'wb')
	pickle.dump(rfmodel, model_pkl)
	model_pkl.close()

if __name__ == "__main__":
	rfmodel(data.preprocess("data","hour.csv"))
