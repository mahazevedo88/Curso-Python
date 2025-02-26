from flask import Flask, redirect, url_for, request, render_template
from requests import get

app = Flask(__name__)

@app.route('/')
def pagina_inicial():
    return render_template('inicio.html')

@app.route('/entrar/')
def fazer_login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run('0.0.0.0')







