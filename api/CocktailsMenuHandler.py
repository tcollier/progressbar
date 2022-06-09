from flask_restful import Api, Resource, reqparse
from clients.SquareupClient import SquareupClient

import json

class CocktailsMenuHandler(Resource):
    def get(self):
        client = SquareupClient()

        return {
            'resultStatus': 'SUCCESS',
            'menuItems': client.getMenu()
        }