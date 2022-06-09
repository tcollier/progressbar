from flask_restful import Api, Resource, reqparse
from flask import request

class InvoiceSettledHandler(Resource):
    def get(self):
        item_id = request.args.get('itemId')
        return {
            'resultStatus': 'SUCCESS',
            'message': "Invoice settled for " + item_id
        }

    def post(self):
        print(self)
        parser = reqparse.RequestParser()
        args = parser.parse_args()

        print(args)
        return {
            'resultStatus': 'SUCCESS',
            'message': "Invoice Settled Handler: "
        }

