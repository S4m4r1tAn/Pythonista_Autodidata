import json

student_ID_json = """{
    "name"     : "John Smith",
    "age"      : 30,
    "city"     : "New York",
    "isStudent": true,
    "gpa"      : 3.5 
}"""

#Lendo um string JSON.  
data = json.loads(student_ID_json)
print(data["name"])

#Salvar um string JSON -> Arquivo JSON.
with open('desafio.json','w',encoding='utf-8') as arquivo_json:
    json.dump(student_ID_json,arquivo_json)

#Ler um arquivo JSON.  
with open('desafio.json',encoding='utf-8') as arquivo_json:
    string_student_json = json.load(arquivo_json)
    dicionario_student_json = json.loads(string_student_json)
    print(dicionario_student_json["isStudent"])
    