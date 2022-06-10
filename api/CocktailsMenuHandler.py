from flask_restful import Api, Resource, reqparse
from clients.SquareupClient import SquareupClient

import json

class CocktailsMenuHandler(Resource):
    def get(self):
        client = SquareupClient()

        menuItems = client.getMenu()

        return {
            'resultStatus': 'SUCCESS',
            'message': "Fetched the menu",
            "menuItems": [item.toJSON() for item in menuItems]
        }

