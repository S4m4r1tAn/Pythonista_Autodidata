from flask import Flask, jsonify, request

app =  Flask(__name__)

postagens = [
    {
        'titulo': 'Minha Historia',
        'autor': 'Amanda Dias'
    },
    {
        'titulo': 'Novo Dispositivo Sony',
        'autor': 'Howard Stringer'
    },
    
    {
        'titulo': 'Lancamento do Ano',
        'autor': 'Jeff Bezos'
    },
]
# Rota padrao - GET https://localhost:5000
@app.route('/')
def obter_postagens():
    return jsonify(postagens)

# Obter postagem por id - GET https://localhost:5000/postagem/1
@app.route('/postagem/<int:indice>', methods=['GET'])
def obter_postagem_por_indice(indice):
    return jsonify(postagens[indice])

# Criar uma nova postagem - POST https://localhost:5000/postagem
@app.route('/postagem', methods=['POST'])
def nova_postagem():
    postagem = request.get_json()
    postagens.append(postagem)

# Alterar uma postagem existente - PUT https://localhost:5000/postagem/1
@app.route('/postagem/<int:indice', methods=['PUT'])
def alterar_postagem(indice):
    postagem_alterada = request.get_json()
    postagens[indice].update(postagem_alterada)
    return jsonify(postagens[indice], 200)

# Excluir uma postagem - DELETE https://localhost:5000/postagem/1
def excluir_postagens(indice):
    try:
        if postagens[indice] is not None:
            del postagens[indice]
            return jsonify(f'Foi excluida a postagem {postagens[indice]}', 200)
    except:
        return jsonify('Nao foi possivel encontrar a postagem para exclusao.', 404)

app.run(port=5000, host='localhost', debug=True)
