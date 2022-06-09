from flask_restful import Api, Resource, reqparse
import json

class CocktailsMenuHandler(Resource):
    def get(self):
        f = open('resources/json/CocktailsMenu.json')
        return json.load(f)
