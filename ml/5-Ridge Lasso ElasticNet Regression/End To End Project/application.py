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

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html') 
    if request.method == 'POST':
        Temperature = request.form['Temperature']
        RH = request.form['RH']
        Ws = request.form['Ws']
        Rain = request.form['Rain']
        FFMC = request.form['FFMC']
        DMC = request.form['DMC']
        ISI = request.form['ISI']
        Classes = request.form['Classes']
        Region = request.form['Region']
        
        scaled_data = scaler.transform([[Temperature, RH, Ws, Rain, FFMC, DMC, ISI, Classes, Region]])
        result = ridge.predict(scaled_data)

        return render_template('index.html', results=result[0])

if __name__=="__main__":
    app.run(host="0.0.0.0") 