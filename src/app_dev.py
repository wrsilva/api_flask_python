from flask import Flask, jsonify
from flask_restx import Api
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST
import api.resource_api as resource_api

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
app.config['JWT_BLACKLIST_ENABLED'] = True

# MySQL configurations.
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
app.config['MYSQL_DATABASE_DB'] = 'db_estudo'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

api = Api(app)
jwt = JWTManager(app)


@jwt.token_in_blocklist_loader
def verifica_blacklist(self, token):
    return token['jti'] in BLACKLIST


@jwt.revoked_token_loader
def token_de_acesso_invalidado():
    # unauthorized
    return jsonify({'message': 'You have been logged out.'}), 401


resource_api.__init__(api)

if __name__ == '__main__':
    # from sql_alchemy import banco
    from sql_settings import mysql
    mysql.init_app(app)
    app.run(debug=True, port=8957)
