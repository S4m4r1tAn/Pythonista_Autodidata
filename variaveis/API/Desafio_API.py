from flask import Flask, jsonify, request
from pprint import pprint

app = Flask(__name__)
cancoes = [
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

app.route('/cancoes', methods=['GET']) #rota padrao: http://localhost:5000
def obter_todas_cancoes():
    return jsonify(cancoes)

@app.route('/cancoes/<int:cancao_id>', methods=['GET']) # Get com Id: http://localhost:5000/cancoes/1
def obter_cancao_por_indice(cancao_id):
    return jsonify(cancoes[cancao_id])

@app.route('/cancoes', methods=['POST']) # Criar uma nova postagem: http://localhost:5000/cancoes
def nova_cancao():
    cancao = request.get_json()
    cancoes.append(cancao)
    return jsonify(f'A cancao: {cancao} foi adicionada com sucesso', 200)

@app.route('/cancoes/<int:cancao_id>', methods=['PUT']) # Alterar uma postagem existente: http://localhost:5000/cancoes/1
def alterar_cancao(cancao_id):
    cancao_alterada = request.get_json()
    cancoes[cancao_id].update(cancao_alterada)
    return jsonify(cancoes[cancao_id], 200)

@app.route('/cancoes/<int:cancao_id>', methods=['DELETE']) # Excluir uma postagem: http://localhost:5000/cancoes/1
def excluir_cancao(cancao_id):
    try:
        del cancoes[cancao_id]
        return jsonify(f'Foi excluida a musica {cancao_id} com sucesso!')
    except:
        jsonify('Nao foi encontrada uma cancao com este id', 404)
    
app.run(port=5000, host='localhost', debug=True)
