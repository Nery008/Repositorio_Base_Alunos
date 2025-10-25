import json

# String no formato Json, usar aspas duplas e os valores booleanos em minúsculo

json_data = '{"nome":"Ana","idade":30,"estudante":true}'

dados_python = json.loads(json_data)

print(dados_python['nome'])
print(dados_python['idade'])
print(dados_python['estudante'])
