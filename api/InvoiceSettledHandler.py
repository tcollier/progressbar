from flask_restful import Api, Resource, reqparse
from flask import request

from clients.SquareupClient import SquareupClient

class InvoiceSettledHandler(Resource):
    def get(self):
        item_id = request.args.get('itemId')
        return {
            'resultStatus': 'SUCCESS',
            'message': "Invoice settled for " + item_id
        }

    def post(self):
        itemId = request.args.get['itemId']
        sqClient = SquareupClient()
        receiptId = sqClient.createOrder(sqClient.getItem(itemId))

        return {
            'resultStatus': 'SUCCESS',
            'message': "Invoice Settled Handler",
            'receiptId': receiptId,
        }

