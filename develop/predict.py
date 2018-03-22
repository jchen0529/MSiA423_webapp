"""

This is the main predict file for predicting bikeshare demand.

Author: Jamie Chen

"""


from sklearn.ensemble import RandomForestRegressor
import pandas as pd
import numpy as np
import pickle
from sklearn.externals import joblib

def predictresponse(input_vals):
	""" Main predict function

	load the random forest model exported from jupyter notebook
	conver user input values into 2D array for model to work with

	:param input_vals: list of user input variables

	"""

	#rfModel = pickle.load((open("rf.pkl", "rb")))
	rfModel = joblib.load("./develop/rf.pkl")
	testdf = pd.DataFrame(np.array([input_vals]),
		columns=["mnth", "hr", "weekday", "weathersit", "temp", "hum","windspeed"])
	modelpred = rfModel.predict(X=testdf)
	occupancy = np.exp(modelpred)/980*100
	return occupancy[0]


#test function
#print(predictresponse([1,2,1,3,0.3,0.6,0.12]))
#0.592
