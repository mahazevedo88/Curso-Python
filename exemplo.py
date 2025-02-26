from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/nome/<nome>', methods=['GET'])
def pegar_nome(nome):
    return(nome)

@app.route('/curso/<curso>', methods=['GET'])
def pegar_curo(curso):
    return(curso)

@app.route ('/')
def inicio():
    frase = "Seja bem vindo, tá funcionando, relax!"
    return frase


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)









