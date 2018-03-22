from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from msiapp import application, db
#from config import SQLALCHEMY_DATABASE_URI
from msiapp.models import hour

import pandas as pd
from develop.predict import predictresponse
import logging

#app = Flask(__name__)

@application.route("/") #root directory, homepage of the website
def index():
	return render_template("test.html")

@application.route("/realtime")
def about():
	return render_template("about.html")

@application.route("/result", methods= ["POST"])
def result():
	user_input = [1,2,3,4,5,6,7]
	user_input[0] = int(request.form.get('month'))
	user_input[1] = int(request.form.get('hour'))
	user_input[2] = int(request.form.get('weekday'))
	user_input[3] = int(request.form.get('weathersit'))
	user_input[4] = int(request.form['temp'])/41
	user_input[5] = int(request.form['hum'])/100
	user_input[6] = int(request.form['wind'])/67

	hour_describe1 = hour(month= request.form.get('month'), 
				hour= request.form.get('hour'), 
				weekday= request.form.get('weekday'), 
				weather_condition = request.form.get('weathersit'), 
				temp = request.form['temp'], 
				humid = request.form['hum'], 
				windspeed = request.form['wind'])
	db.session.add(hour_describe1)
	db.session.commit()

	predict = predictresponse(user_input)
	predict_format = str(round(predict,2)) + '%'
	return render_template("result.html", result = predict_format, hours = hour.query.all())

if __name__ == "__main__":
	#logging.basicConfig(filename='application.log', level=logging.DEBUG)
    #logger = logging.getLogger(__name__) 
	application.run(use_reloader=True, debug=True)