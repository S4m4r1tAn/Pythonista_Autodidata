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
### Iremos utilizar o url base 'localhost' """ #rota padra: http://localhost:5000
app.route('/')
def obter_musicas():
    return jsonify(musicas)

### 3. Quais são os endpoints?
### Disponibilize endpoints para consultar, editar, criar e excluir
# Get com Id - GET http://localhost:5000/musicas/1
@app.route('/musicas/<int:indice>', methods=['GET'])
def obter_musicas_por_indice(indice):
    return jsonify(musicas[indice])

# Criar uma nova postagem - POST http://localhost:5000/cancao
@app.route('/musicas', methods=['POST'])
def nova_musica():
    musica = request.get_json()
    musicas.append(musica)
    return jsonify(musica, 200)

# Alterar uma postagem existente - PUT http://localhost:5000/cancao/1
@app.route('/musica/<int:indice>', methods=['PUT'])
def alterar_musica(indice):
    musica_alterada = request.get_json()
    musicas[indice].update(musica_alterada)
    return jsonify(musicas[indice],200)

# Excluir uma postagem - DELETE - http://localhost:5000/cancao/1
@app.route('/musica/<int:indice>', methods=['DELETE'])
def excluir_musica(indice):
    try:
        if musica[indice] is not None:
            del musicas[indice]
            return jsonify(f'Foi excluida a musica {musicas[indice]}', 200)
    except:
        return jsonify('Nao foi possivel encontrar a musica para exclusao', 404)
    
### 4. Quais recursos serão disponibilizados pela API?
### Informações sobre canções
### 5. Quais verbos http serão disponibilizados?
""" * GET
* POST
* PUT
* DELETE """
### 6. Quais são os URLs completos para cada um?
""" * GET http://localhost:5000/cancoes
* GET http://localhost:5000/cancoes/1
* POST http://localhost:5000/cancoes
* PUT http://localhost:5000/cancoes/1
* DELETE http://localhost:5000/cancoes/1 """
### 7. Qual deve ser a estrutura de cada canção
### - lista de dicionários, que contem cancao e estilo

app.run(port=5000, host='localhost', debug=True)