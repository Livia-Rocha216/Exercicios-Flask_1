from flask import Flask, redirect, render_template

app = Flask(__name__)

# Exercício 1
@app.route('/')
def index():
    return "<h1>Hello, Flask!</h1>"

#Exercício 2
@app.route('/versao')
def versao():
    versao = "1.20.1"
    return f"App v{versao}"

