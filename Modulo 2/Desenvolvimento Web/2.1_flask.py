# Exercício 2.1: HTML básico na resposta
# Modificar sua rota principal para retornar um pequeno html com título,
# parágrafo e um link para outra rota.
# Usar 'render_template' para renderizar uma arquivo .html
# Usar 'url_for()' nas anchor tags do script html

from flask import Flask, render_template

app = Flask(__name__)  # representa o nome do arquivo

@app.route('/')  # rota principal, que é a rota index ('/')
def home():
    return render_template('ex_2-1.html')  # a biblioteca render_template "lê" o html

@app.route('/sobre')  # nova rota
def sobre():
    return 'Fábrica de Programadores'

@app.route('/zezinho')  # nova rota
def zezinho():
    return 'Achou a rota'

if __name__ == '__main__':
    app.run(debug=True)
