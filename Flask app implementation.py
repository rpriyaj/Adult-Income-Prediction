import flask
from flask import request
import numpy as np
import pickle
app = flask.Flask(__name__)
app.config["DEBUG"] = True
pickle_in = open('rcart.pkl','rb')


classifier = pickle.load(pickle_in)

from flask_cors import CORS
CORS(app)

@app.route('/')
def home():
    return '<h1> home page </h1>'




@app.route('/predict')
def predict():
    age = request.args.get('age')
    education_number = request.args.get('education_number')
    marital = request.args.get('marital')
    occupation = request.args.get('occupation')
    race = request.args.get('race')
    sex = request.args.get('sex')
    capitalgain = request.args.get('capitalgain')
    capitalloss = request.args.get('capitalloss')
    hours = request.args.get('hours')
    country = request.args.get('country')
    prediction = classifier.predict([[age, education_number, marital, occupation, race, sex, capitalgain, capitalloss, hours, country]])
    return "Predicted adult income will be" + str(prediction)
  



if __name__ == '__main__':
    app.run()
