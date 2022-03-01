import sklearn
import joblib
import pandas as pd
import numpy as np
from fonctions_maison import extraire_la_premiere_lettre
from flask import Flask ,request

pipeline=joblib.load('titanic.model')

#print(pipeline)

#demarrer l'aplication flask
app=Flask('__name__')

#page dacueil
@app.route('/')
def index():
    return "<h1>Bienven,ue dans notre API. Utiliser /predict en post pour faire des predictions sur Titanic </h1>"


#tester l'api'
@app.route('/ping', methods=['GET'])
def ping():
    return ("pong", 200)


@app.route('/predict', methods=["POST"])
def predict():
    df=pd.DataFrame(request.json)
    resulats=pipeline.predict(df)[0]
    return (str(resulats),201)

#lancer et executer lapi
if  __name__=="__main__":
    app.run()
