from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        return {'message': 'user 1 '}

class User(Resource):
    def post(self):
        return {'message': 'teste'}
    
    def get(self):
        return {'message': 'CPF'}

api.add_resource(Users, '/users')
api.add_resource(User, '/user', '/user/<string:cpf>')

if __name__ == '__main__':
    app.run(debug=True)

# Rodar a aplicação utilizando o comando "flask run"
# localhost: http://127.0.0.1:5000/