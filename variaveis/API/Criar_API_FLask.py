# Nosso 1º API - FLASK
# FLASK & FLASK RESTFUL
from flask import Flask, jsonify, request

app = Flask(__name__)
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
    }
]
# Rota padrao - GET http://localhost:5000
@app.route('/')
def obter_postagens():
    return jsonify(postagens)

app.run(port=5000, host='localhost', debug=True)