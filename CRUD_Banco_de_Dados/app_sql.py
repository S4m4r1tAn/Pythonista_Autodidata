from flask import Flask, jsonify, request
from estrutura_banco_de_dados import Autor, Postagem, app, db

# Rota padrão - GET https://localhost:5000
@app.route('/')
def obter_postagens():
    return jsonify(postagens)

# Obter postagem por id - GET https://localhost:5000/postagem/1
@app.route('/postagem/<int:indice>', methods=['GET'])
def obter_postagem_por_indice(indice):
    return jsonify(postagens[indice])

# Criar uma nova postagem - POST https://localhost:5000/postagem
@app.route('/postagem',methods=['POST'])
def nova_postagem():
    postagem = request.get_json()
    postagens.append(postagem)

    return jsonify(postagem, 200)

# Alterar uma postagem existente - PUT https://localhost:5000/postagem/1
@app.route('/postagem/<int:indice>',methods=['PUT'])
def alterar_postagem(indice):
    postagem_alterada = request.get_json()
    postagens[indice].update(postagem_alterada)

    return jsonify(postagens[indice], 200)

# Excluir uma postagem - DELETE - https://localhost:5000/postagem/1
def excluir_postagem(indice):
    try:
        if postagens[indice] is not None:
            del postagens[indice]
            return jsonify(f'Foi excluído a postagem {postagens[indice]}',200)
    except:
        return jsonify('Não foi possível encontrar a postagem para exclusão',404)


@app.route('/autores')
def obter_autores():
    autores = Autor.query.all()
    lista_de_autores = []
    for autor in autores:
        autor_atual = {}
        autor_atual['id_autor'] = autor.id_autor
        autor_atual['nome'] = autor.nome
        autor_atual['email'] = autor.email
        lista_de_autores.append(autor_atual)
        
    return jsonify({'autores': lista_de_autores})

@app.route('/autores/<int:id_autor>',methods=['GET'])
def obter_autor_por_id(id_autor):
    pass

@app.route('/autores',methods=['POST'])
def novo_autor():
    pass

@app.route('/autores/<int:id_autor>',methods=['PUT'])
def alterar_autor(id_autor):
    pass

@app.route('/autores/<int:id_autor>',methods=['DELETE'])
def excluir_autor(id_autor):
    pass


app.run(port=5000,host='localhost',debug=True)
