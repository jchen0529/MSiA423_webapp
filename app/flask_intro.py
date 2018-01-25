from flask import Flask, render_template
app = Flask(__name__)

@app.route("/profile/<username>")
def profile (username):
	return '<h2>Hey there %s</h2>' % username

if __name__ == "__main__":
	app.run(debug=True)
