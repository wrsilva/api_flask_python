from flask_restx import fields
from api.server.instance import server

person = server.api.model('Person',{
    'age' : fields.Integer(description='Idade da pessoa', required = True),
    'first_name' : fields.String(description='Primeiro nome', required = True),
    'last_name' : fields.String(description='Segundo nome', required = True)
})

personById = server.api.model('PersonById',{
    'id_person' : fields.Integer(description='Id da pessoa', required = True),
    'age' : fields.Integer(description='Idade da pessoa', required = True),
    'first_name' : fields.String(description='Primeiro nome', required = True),
    'last_name' : fields.String(description='Segundo nome', required = True)
})

class PersonEntity:
    id_person: int
    age: int
    first_name: str
    last_name: str
    
    def __init__(self,
                 id_person: int,
                 age: int,
                 first_name: str,
                 last_name: str):
        self.id_person = id_person
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def json(self):
        return {
            'age': self.age,
            'first_name': self.first_name,
            'last_name': self.last_name
        }
