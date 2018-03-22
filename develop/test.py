import pytest
from data import preprocess	
from predict import predictresponse
import pandas as pd

#Test the following functions by checking if the function output matches with the desired
def preprocess(datafolder,filename):
	inpath = "data"
	infilename = "hour.csv"
	data = preprocess(inpath, infilename)
	assert type(data) is pd.core.frame.DataFrame
	assert type(data["weekday"]) == "category"


test = [3,7,3,1,20,30,10]

def predictresponse(input_vals):
	result = predictresponse(test)
	assert len(result) == 1
	assert type(result) is float