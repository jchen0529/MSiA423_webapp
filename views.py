from flask import Flask, render_template, request
from app import app
import pandas as pd
from develop.predict import predictresponse

#app = Flask(__name__)

@app.route("/")
def index():
	return render_template("test.html")

@app.route("/realtime")
def about():
	return render_template("about.html")

@app.route("/result", methods= ["POST"])
def result():
	user_input = [1,2,3,4,5,6,7]
	user_input[0] = int(request.form.get('month'))
	user_input[1] = int(request.form.get('hour'))
	user_input[2] = int(request.form.get('weekday'))
	user_input[3] = int(request.form.get('weathersit'))
	user_input[4] = int(request.form['temp'])/41
	user_input[5] = int(request.form['hum'])/100
	user_input[6] = int(request.form['wind'])/67
	predict = predictresponse(user_input)
	predict_format = str(round(predict,2)) + '%'
	return render_template("result.html", result = predict_format)

if __name__ == "__main__":
	app.run(use_reloader=True, debug=True)