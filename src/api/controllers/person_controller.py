
from api.entity.person_entity import PersonEntity
from flask_restx import Resource, reqparse
from api.db.person_scripts import APOSTA_HISTORY, APOSTA_INSERT
from sql_settings import mysql


class PersonController(Resource):

    def post(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            aposta_params = reqparse.RequestParser()
            aposta_params.add_argument('fist_name', type=str)
            aposta_params.add_argument('last_name', type=str)
            aposta_params.add_argument('age', type=int, required=True)

            aposta_args = aposta_params.parse_args()
            aposta = PersonEntity(**aposta_args)

            params = (
                str(aposta.age),
                str(aposta.fist_name),
                str(aposta.last_name)
            )
            cursor.execute(APOSTA_INSERT, params)
            conn.commit()

            return PersonEntity.json(aposta)

        except Exception as e:
            return {"mesage": "{}".format(e)}, 404

    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(APOSTA_HISTORY)

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
