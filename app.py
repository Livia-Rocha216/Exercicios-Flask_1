from flask import Flask, redirect, render_template

app = Flask(__name__)

# Exercício 1
@app.route('/')
def index():
    return "<h1>Hello, Flask!</h1>"

# Exercício 2
@app.route('/versao')
def versao():
    versao = "1.20.1"
    return f"App v{versao}"

# Exercício 3
@app.route('/saudar/<nome>')
def saudar(nome):
    return f"Olá, {nome.capitalize()}"

# Exercício 4
@app.route('/quadrado/<int:n>')
def quadrado(n):
    return f"{n}² = {n * n}"

# Exercício 5
@app.route('/home')
def home():
    return redirect('/')

# Exercício 6
@app.route('/pagina')
def pagina():
    return render_template('index.html')

# Exercício 7
@app.route('/buscar/<item>')
def buscar(item):
    itens = ["sapato", "calça", "chapéu", "óculos"]
    for it in itens:
        if it != item:
            return f"O item {item.capitalize()} não foi encontrado."
        else:
            return f"O item {item.capitalize()} foi encontrado!"