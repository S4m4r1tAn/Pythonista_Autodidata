import json
#Imprimir email do usuario id 2.
with open('desafio.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json) # Converter arquivo JSON -> String
    print(data["user"][0]["email"])

#Imprimir a city do id 1.
with open('desafio.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data["user"][1]["address"]["city"])
    
#Imprimir o total do pedido do id 2.
with open('desafio.json', encoding='utf-8') as arquivo_json:
    data = json.load(arquivo_json)
    print(data["user"][1]["orders"][0]["total"])
