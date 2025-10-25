# Lendo um arquivo do tipo JSON
# Sempre iniciamos com a importação do json ou da biblioteca que utilizaremos
import json

# Abriremos o arquivo e o modo "r" lê esse arquivo
with open("dados.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)  # json.load (sem o "s") lê diretamente de um arquivo

# Exibindo o conteúdo
print(dados)
print(type(dados))
