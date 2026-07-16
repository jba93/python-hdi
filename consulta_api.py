import json, requests

resultado = requests.get("https://servicodados.ibge.gov.br/api/v2/censos/nomes/juliana")

dados_json = json.loads(resultado.text)

print(dados_json[0]["res"][2])