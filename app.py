from flask import Flask, jsonify
from flask_restful import Resource, Api, reqparse
from flask_mongoengine import MongoEngine
import os


app = Flask(__name__)


app.config['MONGODB_SETTINGS'] = {
    'db': 'users',
    'host': 'mongodb',
    'port': 27017,
    'username': os.getenv('MONGO_DB_USERNAME'),
    'password': os.getenv('MONGO_DB_PASSWORD'),
}


_user_parser = reqparse.RequestParser()
_user_parser.add_argument('name',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('last_name',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('cpf',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('email',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )
_user_parser.add_argument('birth_date',
                          type=str,
                          required=True,
                          help="This field cannot be blank."
                          )

api = Api(app)
db = MongoEngine(app)


#  Classe que irá se conectar com o Banco MongoDB
class UserModel(db.Document):
    cpf = db.StringField(required=True, unique=True)  # PK
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.EmailField(required=True)
    birth_date = db.DateTimeField(required=True)


class Users(Resource):
    def get(self):
        #return jsonify(UserModel.objects())
        return {"message": "user 1"}


class User(Resource):
    def post(self):
        data = _user_parser.parser_args()
        return data

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