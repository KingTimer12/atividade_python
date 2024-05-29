from flask import Flask, request
from flask_cors import CORS # type: ignore
from database import insert, fetch_all, fetch_one, delete

app = Flask(__name__)
CORS(app)

@app.route("/notas", methods=['POST'])
def telefones_create():
    nome: str = request.json["nome"]
    notas: list[int] = request.json["notas"]
    insert((nome, notas))
    return request.json, 200

@app.route("/notas", methods=['GET'])
def telefones_fetch():
    if 'nome' in request.args:
        nome: str = request.args['nome']
        return fetch_one(nome)
    return fetch_all()

@app.route("/notas", methods=['DELETE'])
def telefones_delete():
    if 'nome' in request.args:
        nome: str = request.args['nome']
        delete((nome,))
        return '', 204
    delete()
    return '', 204