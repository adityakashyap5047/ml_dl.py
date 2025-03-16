from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

### Loading the StandardScaler and Ridge Regression Pickle file
ridge = pickle.load(open('models/ridge.pkl', 'rb'))
scaler = pickle.load(open('models/scaler.pkl', 'rb'))

@app.route("/")
def hello_world():
    return "Hello World"


if __name__=="__main__":
    app.run(host="0.0.0.0")