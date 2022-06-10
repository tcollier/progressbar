from flask_restful import Resource

from clients.BtcPayServerClient import BtcPayServerClient


class CreateInvoiceHandler(Resource):
    def get(self):
        invoice_url = BtcPayServerClient().create_invoice()
        return invoice_url

    def post(self):
        print(self)

