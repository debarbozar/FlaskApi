from flask import Flask
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine

app = Flask(__name__)

#inicializador api 
api = Api(app)

#inicializador db
db = MongoEngine(app)

#Confiuração MongoDB
app.config['MONGODB_SETTINGS'] = {
    'db': 'users',
    'host': 'mongodb',
    'port': 27017,
    'user': 'admin',
    'password': 'admin',
}


class Users(Resource):
    def get(self):
        return {"message": "user 1 "}


class User(Resource):
    def post(self):
        return {"message": "teste"}

    def get(self):
        return {"message": "CPF"}


api.add_resource(Users, "/users")
api.add_resource(User, "/user", "/user/<string:cpf>")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")

"""
Impacto:
    Necessario utilizar o host "0.0.0.0" pois ao chamar a 
    aplicação no docker não estava pegando o IP do container, e sim somente local
    Sendo assim só está recebendo conexão em uma interface (lookback).
"""
