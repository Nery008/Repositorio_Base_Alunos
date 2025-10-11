# Passe uma lista de nomes para o template e use um for em Jinja para listar todos os nomes em uma <ul>
# lista não ordenada

from flask import Flask, render_template
app = Flask(__name__)  # representa o nome do arquivo

@app.route('/')  # @decorador de função
def index():
    return 'Hello Flask!'

@app.route('/sobre')
def sobre():
    return 'Olá, eu sou aluno do projeto Fábrica de Programadores.'

@app.route('/lista')
def lista():
    alunos = ['Isabela', 'Yasmin', 'Eduarda', 'Gabrielle', 'Beatriz', 'Vinicius', 'Ana Livia']
    return render_template('ex_3-2.html', lista=alunos)

if __name__ == '__main__':
    app.run(debug=True)
