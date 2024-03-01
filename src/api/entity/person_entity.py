from flask_restx import fields
from api.server.instance import server

person = server.api.model('Person',{
    'age' : fields.String(description='Idade da pessoa', required = True, type= int),
    'fist_name' : fields.String(description='Primeiro nome', required = True),
    'last_name' : fields.String(description='Segundo nome', required = True)
})

class PersonEntity:
    age: int
    fist_name: str
    last_name: str
    
    def __init__(self,
                 age: int,
                 fist_name: str,
                 last_name: str):
        self.age = age
        self.fist_name = fist_name
        self.last_name = last_name

    def json(self):
        return {
            'age': self.age,
            'fist_name': self.fist_name,
            'last_name': self.last_name
        }
