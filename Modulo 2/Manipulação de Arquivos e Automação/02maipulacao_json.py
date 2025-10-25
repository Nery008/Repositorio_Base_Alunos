# importar o json
import json

# criar um dicionário Python
dados = {
    "nome": "Maria",
    "idade": 30,
    "cursos": ["Python", "Machine Learning"]
}

# Criar um arquivo Json e escrever dentro dele
with open('dados.json', 'w', encoding='utf-8') as arquivo:  # w é o modo para escrever,
    # encoding é para ortografia utilizar os caracteres especiais
    json.dump(dados, arquivo, indent=4, ensure_ascii=False)  # json.dump converte um dicionario em json e grava no arquivo
