
from api.entity.person_entity import PersonEntity, person, personById
from flask_restx import Resource, reqparse
from api.db.person_scripts import PERSON_INSERT, PERSON_HISTORY, PERSON_DELETE
from sql_settings import mysql
from api.server.instance import server

app,api = server.app, server.api


parser_id_person = reqparse.RequestParser()
parser_id_person.add_argument("id_person", required=True, type=int, action="store")

@api.route('/person')
class PersonController(Resource):

    @api.expect(person, valitade = True)
    @api.marshal_with(personById)
    def post(self,):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            response = api.payload
            
            person = PersonEntity(**response)
            
            params = (
                str(person.age),
                str(person.first_name),
                str(person.last_name)
            )
            cursor.execute(PERSON_INSERT, params)
            conn.commit()

            api.logger.debug(person)
            return person, 201
            # return PersonEntity.json(person), 201

        except Exception as e:
            return {"mesage": "{}".format(e)}, 500

    @api.marshal_list_with(personById)
    def get(self,):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()

            cursor.execute(PERSON_HISTORY)

            resultado = cursor.fetchall()
            listOfPerson = []

            if resultado:
                for linha in resultado:
                    listOfPerson.append(
                        {
                            'id_person': linha[0],
                            'age': linha[1],
                            'first_name': str(linha[2]),
                            'last_name': str(linha[3])
                        })

            return listOfPerson
        except Exception as e:
            return {"mesage": "{}".format(e)}, 500
    
    @api.expect(parser_id_person)
    def delete(self,):
        try:
            id_person: int = parser_id_person.parse_args()['id_person']
            conn = mysql.connect()
            cursor = conn.cursor()
            
            params = (
                id_person
            )

            cursor.execute(PERSON_DELETE, params)
            conn.commit()

            resultado = cursor.fetchall()
            return 'sucess',200
        except Exception as e:
            return {"mesage": "{}".format(e)}, 500
