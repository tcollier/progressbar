from flask_restful import Api, Resource, reqparse
import json

class CocktailMenuHandler(Resource):
    def get(self):
        f = open('resources/json/CocktailMenu.json')
        return json.load(f)
