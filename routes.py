import requests
from flask import Flask, render_template, request, redirect
import pandas as pd
import quandl
from bokeh.plotting import figure, show, reset_output
from bokeh.charts import TimeSeries
from bokeh.palettes import Spectral11
from bokeh.embed import components 
from forms import SignupForm



quandl.ApiConfig.api_key = 'xx15tPCkmMzchc5HW3mp'

app = Flask(__name__)

app.secret_key = "development-key"

TOOLS = "pan,wheel_zoom,box_zoom,reset"

numlines = 2
mypalette=Spectral11[0:numlines]

print('inside app')
@app.route("/")
def index():
  print('at /')
  return render_template("index.html")

@app.route("/about")
def about():
  return render_template("about.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
	print('in signup')
	form = SignupForm()
	if request.method == 'POST':
		if form.validate() == False:
			return render_template('signup.html', form=form)
		else:

			return  render_template("firstDerivative_color_scatter.html")

	elif request.method == "GET":
		return render_template('signup.html', form=form)


if __name__ == "__main__":
 	app.run()
