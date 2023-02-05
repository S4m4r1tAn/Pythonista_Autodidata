from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurações inicias
app.config['SECRET_KEY'] = 'segredo2030'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app)
db: SQLAlchemy


class Postagem(db.Model):
    __tablename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor'))


class Autor(db.Model):
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    postagens = db.relationship('Postagem')


# db.drop_all()
# db.create_all()
# autor = Autor(nome='Jhonatan', email='jhonatan@hotmail.com',
#               senha='senha123', admin=True)
# db.session.add(autor)
# db.session.commit()


@app.route('/postagens', methods=['GET'])
def obter_todas_postagens():
    return jsonify(postagens)


@app.route('/postagens/<int:postagem_id>', methods=['GET'])
def obter_postagem_por_id(postagem_id):
    return jsonify(postagens[postagem_id])


@app.route('/postagens', methods=['POST'])
def nova_postagem():
    postagem = request.get_json()
    postagens.append(postagem)
    return jsonify({'mensagem': 'recurso criado com sucessso'}), 200


@app.route('/postagens/<int:postagem_id>', methods=['PUT'])
def atualizar_postagem(postagem_id):
    resultado = request.get_json()
    postagens[postagem_id].update(resultado)
    return jsonify(postagens[postagem_id]), 200


@app.route('/postagens/<int:postagem_id>', methods=['DELETE'])
def excluir_postagem(postagem_id):
    postagem = postagens[postagem_id]
    del postagens[postagem_id]
    return jsonify({'mensagem': 'A postagem foi excluída com sucesso!'})


if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
