from flask import Flask, render_template, make_response, request, jsonify
from flask_pydantic import validate
import pandas as pd
import numpy as np
import json
import pickle
import base64




identification = {"alice": "d29uZGVybGFuZA==", "bob": "YnVpbGRlcg==", "clementine": "bWFuZGFyaW5l"}
username_liste = list(identification.keys())


log_newton_model = pickle.load(open('log_newton_model.pkl','rb'))
log_liblinear_model = pickle.load(open('log_liblinear_model.pkl','rb'))
knc_model = pickle.load(open('knc_model.pkl','rb'))

log_newton_score = "84.61%"
log_liblinear_score = "84.72%"
knc_score = "82.97%"


app = Flask(__name__)

@app.route("/status")
def status():
    return make_response('1\n',200)



@app.route("/Authorization")
@validate()
def authorization():
    x = request.headers.get("Authorization")
    z = x.split("=")
    k=0
    if z[0] == username_liste[0] : 
        k=1
        pwd_encoded = base64.b64encode(z[1].encode("ascii")).decode("ascii")
        if pwd_encoded== identification["alice"] : 
            return "identification reussie\n"
        else :
                return make_response("mot de passe incorrect\n",400)

    if z[0] == username_liste[1] : 
        k=1
        pwd_encoded = base64.b64encode(z[1].encode("ascii")).decode("ascii")
        if pwd_encoded == identification["bob"] : 
            return "identification reussie\n"
        else :
                return make_response("mot de passe incorrect\n",400)
    
    if z[0] == username_liste[2] : 
        k=1
        pwd_encoded = base64.b64encode(z[1].encode("ascii")).decode("ascii")
        if pwd_encoded == identification["clementine"] : 
            return "identification reussie\n"
        else :
                return make_response("mot de passe incorrect\n",400)

    if k == 0 :
        return make_response("nom d'utislisateur incorrect\n",400)


@app.route("/log_newton")
@validate()
def get_performances_log_newton():
    x = request.headers.get("Authorization")
    z = x.split("=")
    pwd_encoded = base64.b64encode(z[1].encode("ascii")).decode("ascii")
    if (z[0] == username_liste[0] and pwd_encoded== identification["alice"]) or (z[0] == username_liste[1] and pwd_encoded== identification["bob"]) or (z[0] == username_liste[2] and pwd_encoded== identification["clementine"]) :
        return make_response('Le score du modele sur le jeu de test est {}\n '.format(log_newton_score),200)



@app.route("/predict1",methods=["POST"])
@validate()
def predict1():
    x = request.headers.get("Authorization")
    z = x.split("=")
    pwd_encoded = base64.b64encode(z[1].encode("ascii")).decode("ascii")
    if (z[0] == username_liste[0] and pwd_encoded== identification["alice"]) or (z[0] == username_liste[1] and pwd_encoded== identification["bob"]) or (z[0] == username_liste[2] and pwd_encoded== identification["clementine"]) :
        data = request.get_json(force=True)
        df1 = pd.json_normalize(data)
        prediction = log_newton_model.predict([df1.iloc[0].astype(int)])
        if prediction[0] == 0 :
            return make_response('Pas de pluie demain\n ',200)
        else :
            return  make_response('Pluie prevue demain\n ',200)

@app.route("/log_liblinear")
@validate()
def get_performances_log_liblinear():
    x = request.headers.get("Authorization")
    z = x.split("=")
    pwd_encoded = base64.b64encode(z[1].encode("ascii")).decode("ascii")
    if (z[0] == username_liste[0] and pwd_encoded== identification["alice"]) or (z[0] == username_liste[1] and pwd_encoded== identification["bob"]) or (z[0] == username_liste[2] and pwd_encoded== identification["clementine"]) :
        return make_response('Le score du modele sur le jeu de test est {}\n '.format(log_liblinear_score),200)


@app.route("/predict2",methods=["POST"])
@validate()
def predict2():
    x = request.headers.get("Authorization")
    z = x.split("=")
    pwd_encoded = base64.b64encode(z[1].encode("ascii")).decode("ascii")
    if (z[0] == username_liste[0] and pwd_encoded== identification["alice"]) or (z[0] == username_liste[1] and pwd_encoded== identification["bob"]) or (z[0] == username_liste[2] and pwd_encoded== identification["clementine"]) :
        data = request.get_json(force=True)
        df1 = pd.json_normalize(data)
        prediction = log_newton_model.predict([df1.iloc[0].astype(int)])
        if prediction[0] == 0 :
            return make_response('Pas de pluie demain\n ',200)
        else :
            return  make_response('Pluie prevue demain\n ',200)


@app.route("/knc")
@validate()
def get_performances_knc():
    x = request.headers.get("Authorization")
    z = x.split("=")
    pwd_encoded = base64.b64encode(z[1].encode("ascii")).decode("ascii")
    if (z[0] == username_liste[0] and pwd_encoded== identification["alice"]) or (z[0] == username_liste[1] and pwd_encoded== identification["bob"]) or (z[0] == username_liste[2] and pwd_encoded== identification["clementine"]) :
        return make_response('Le score du modele sur le jeu de test est {}\n'.format(knc_score),200)



@app.route("/predict3",methods=["POST"])
@validate()
def predict3():
    x = request.headers.get("Authorization")
    z = x.split("=")
    pwd_encoded = base64.b64encode(z[1].encode("ascii")).decode("ascii")
    if (z[0] == username_liste[0] and pwd_encoded== identification["alice"]) or (z[0] == username_liste[1] and pwd_encoded== identification["bob"]) or (z[0] == username_liste[2] and pwd_encoded== identification["clementine"]) :
        data = request.get_json(force=True)
        df1 = pd.json_normalize(data)
        prediction = log_newton_model.predict([df1.iloc[0].astype(int)])
        if prediction[0] == 0 :
            return make_response('Pas de pluie demain\n ',200)
        else :
            return  make_response('Pluie prevue demain\n ',200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)