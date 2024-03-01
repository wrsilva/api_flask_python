from flask import Flask
from flask_restx import Api
from flask_jwt_extended import JWTManager
from sql_settings import mysql


class Server():
    def __init__(self,):
        self.app = Flask(__name__)
        self.api = Api(self.app,
            default= 'API Person',
            version='1.0',
            title='Sample Person API',
            description='A simple book API',
            doc='/docs'
        )
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.app.config['JWT_SECRET_KEY'] = 'DontTellAnyone'
        self.app.config['JWT_BLACKLIST_ENABLED'] = True

        # MySQL configurations.
        self.app.config['MYSQL_DATABASE_USER'] = 'root'
        self.app.config['MYSQL_DATABASE_PASSWORD'] = '123456'
        self.app.config['MYSQL_DATABASE_DB'] = 'db_estudo'
        self.app.config['MYSQL_DATABASE_HOST'] = 'localhost'
        
      
        self.jwt = JWTManager(self.app)
        mysql.init_app(self.app)

        
    def run(self,):
        self.app.run(debug=True, port=8957)
        
server = Server()