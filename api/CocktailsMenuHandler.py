from flask_restful import Api, Resource, reqparse
from clients.SquareupClient import SquareupClient

import json

class CocktailsMenuHandler(Resource):
    def get(self):
        client = SquareupClient()
        client.list_catalog_items()
        return {
            'resultStatus': 'SUCCESS',
            'message': "Fetched the menu"
        }
        #f = open('resources/json/CocktailsMenu.json')
        #return json.load(f)