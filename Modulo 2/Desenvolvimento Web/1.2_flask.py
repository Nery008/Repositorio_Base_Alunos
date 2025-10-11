# Exercicio 1.2: Rota personalizada
# Adicione uma nova rota /sobre que retorna uma mensagem com seu nome
# e uma frase sobre você

from flask import Flask
app = Flask(__name__)  # representa o nome do arquivo

@app.route('/')  # @decorador de função
def home():
    return "Olá Mundo!"

@app.route('/sobre')
def sobre():
    return 'Olá, meu nome Nery e odeio programação'

if __name__ == '__main__':
    app.run(debug=True)
