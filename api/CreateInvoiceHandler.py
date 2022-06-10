from flask_restful import Resource
from flask import request

from clients.BtcPayServerClient import BtcPayServerClient


class CreateInvoiceHandler(Resource):
    def get(self):
        item_id = request.args.get('itemId')
        item_price = request.args.get('itemPrice')
        invoice_url = BtcPayServerClient().create_invoice(item_id, item_price)
        return invoice_url

    def post(self):
        print(self)

