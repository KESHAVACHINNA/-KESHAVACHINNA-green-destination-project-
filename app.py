from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

contract_mapping = {
    'Month-to-month': 0,
    'One year': 1,
    'Two year': 2
}

internet_mapping = {
    'DSL': 0,
    'Fiber optic': 1,
    'No': 2
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    tenure = float(request.form['tenure'])
    monthlycharges = float(request.form['monthlycharges'])
    totalcharges = float(request.form['totalcharges'])
    contract = contract_mapping[request.form['contract']]
    internetservice = internet_mapping[request.form['internetservice']]

    final_features = np.array([[tenure, monthlycharges, totalcharges, contract, internetservice]])

    prediction = model.predict(final_features)[0]
    
    output = "Churn" if prediction == 1 else "Not Churn"

    return render_template('index.html', prediction=output)

if __name__ == '__main__':
    app.run(debug=True)
