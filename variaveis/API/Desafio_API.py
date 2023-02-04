from flask import Flask, jsonify, request
from pprint import pprint

### DESAFIO API músicas 🥇
### 1. Definir o objetivo da API:
""" Iremos montar uma api de músicas, onde deverá ser possível, 
consultar todas canções disponíveis, consultar uma canção individual, 
editar canções existentes e também excluir músicas existentes. """
app = Flask(__name__)
musicas = [
     {
     "cancao": "Amor I Love you!",
     "estilo": "MPB"
     },
     {
     "cancao": "A gente se entrega.",
     "estilo": "SERTANEJO"
    },
    {
     "cancao": "Diario de um detento.",
     "estilo": "RAP"
    }
]
### 2. Qual será o URL base da API?
""" Iremos utilizar o url base 'localhost' """ #rota padra: http://localhost:5000
app.route('/')
def obter_musicas():
    return jsonify(musicas)

# Get com Id - GET http://localhost:5000/postagem/1
@app.route('/musicas/<int:indice>', methods=['GET'])
def obter_musicas_por_indice(indice):
    return jsonify(musicas[indice])
### 3. Quais são os endpoints?
""" Disponibilize endpoints para consultar, editar, criar e excluir
### 4. Quais recursos serão disponibilizados pela API?
Informações sobre canções
### 5. Quais verbos http serão disponibilizados?
* GET
* POST
* PUT
* DELETE
### 6. Quais são os URLs completos para cada um?
* GET http://localhost:5000/cancoes
* GET http://localhost:5000/cancoes/1
* POST http://localhost:5000/cancoes
* PUT http://localhost:5000/cancoes/1
* DELETE http://localhost:5000/cancoes/1 """
### 7. Qual deve ser a estrutura de cada canção
### - lista de dicionários, que contem cancao e estilo
 