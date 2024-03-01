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
