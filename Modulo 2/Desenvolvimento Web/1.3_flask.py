# Exercicio 1.3: Parâmetros na URL (rotas dinâmicas)
# Crie uma rota /saudacao/<nome> que retorne "Olá, <nome>! Seja bem-vindo!"

from flask import Flask
app = Flask(__name__)  # representa o nome do arquivo

@app.route('/')  # @decorador de função
def home():
    return "Olá Mundo!"

@app.route('/sobre')
def sobre():
    return 'Olá, meu nome é Nery e odeio programação.'

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return f'Olá {nome}! Seja bem-vindo(a)!'

if __name__ == '__main__':
    app.run(debug=True)
