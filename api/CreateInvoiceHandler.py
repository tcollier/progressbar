from flask_restful import Resource

from clients.BtcPayServerClient import BtcPayServerClient


class CreateInvoiceHandler(Resource):
    def get(self):
        BtcPayServerClient().create_invoice()
        return {
            'resultStatus': 'SUCCESS',
            'message': "Create Invoice Handler"
        }

    def post(self):
        print(self)

