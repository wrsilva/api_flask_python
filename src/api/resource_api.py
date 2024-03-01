from api.controllers.person_controller import PersonController

resouce_v1 = '/api/v1'


def __init__(api):
    api.add_resource(PersonController, resouce_v1+'/person')
