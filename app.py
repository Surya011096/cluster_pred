import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import matplotlib.pyplot as plt
import pandas as pd
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    
    #int_features = [int(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    #prediction = model.predict(final_features)
    
    if request.method == 'POST':
        result=model.resultData

    #output = round(prediction[0], 2)

    return render_template('index.html', prediction_text=' is {}'.format(result))
    
    
    
    
'''
@app.route("/tables")
def show_tables():
    return render_template('view.html',tables=[frame.to_html(classes='3month'), frame1.to_html(classes='predicted_1month')],
    titles = ['na', 'frame', 'frame1_predicted'])
'''
if __name__ == "__main__":
    app.run(debug=True)
