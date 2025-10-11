# Exercicio 3.1: Templates com variáveis
# Modifique o template para receber o nome como variável e exibir "Bem-Vindo, {{nome}}!"

from flask import Flask, render_template
app = Flask(__name__)  # representa o nome do arquivo

@app.route('/')  # @decorador de função
def home():
    return render_template('ex_2-2.html')

@app.route('/sobre')
def sobre():
    return 'Olá, eu sou aluno do projeto Fábrica de Programadores.'

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return render_template('ex_3-1.html', nome= nome)

@app.route('/dobro/<int:numero>')
def dobro(numero):
    return f'O dobro do {numero} é {2*numero}.'

if __name__ == '__main__':
    app.run(debug=True)

