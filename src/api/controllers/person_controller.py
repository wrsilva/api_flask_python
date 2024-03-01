
from api.entity.person_entity import PersonEntity, person
from flask_restx import Resource
from api.db.person_scripts import PERSON_INSERT, PERSON_HISTORY
from sql_settings import mysql
from api.server.instance import server

app,api = server.app, server.api


@api.route('/person')
class PersonController(Resource):

    @api.expect(person,valitade = True)
    @api.marshal_list_with(person)
    def post(self,):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            response = api.payload
            
            person = PersonEntity(**response)

            params = (
                str(person.age),
                str(person.fist_name),
                str(person.last_name)
            )
            print('params ***')
            print(params)
            cursor.execute(PERSON_INSERT, params)
            conn.commit()

            return PersonEntity.json(person)

        except Exception as e:
            return {"mesage": "{}".format(e)}, 404

    @api.marshal_list_with(person)
    def get(self,):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(PERSON_HISTORY)

            resultado = cursor.fetchall()
            mercados = []

            if resultado:
                for linha in resultado:
                    mercados.append(
                        {
                            'aposta_id': linha[0],
                            'fist_name': str(linha[1])
                        })

            return mercados
        except Exception as e:
            return {"mesage": "{}".format(e)}, 404
