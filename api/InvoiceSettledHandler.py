from flask_restful import Api, Resource, reqparse

from clients.BtcPayServerClient import BtcPayServerClient


class InvoiceSettledHandler(Resource):
    # Authorization: Basic
    # dmJPVmswRUVsT2xXaW9DTHZMUW5XMFpPclV2MEUwMFF5UlUwMTA3REJvcg ==
    #
    # vbOVk0EElOlWioCLvLQnW0ZOrUv0E00QyRU0107DBor
    def get(self):
        client = BtcPayServerClient()
        store_id = 'LfUdzH3JMZjcr3mb576bqM9YmQPgwmj1fSTLP7mTXZ7'
        order_id = 1;
        client.create_invoice(store_id, order_id)
        return {
            'resultStatus': 'SUCCESS',
            'message': "Create Invoice Handler"
        }

    def post(self):
        print(self)
        parser = reqparse.RequestParser()
        args = parser.parse_args()

        print(args)
        # note, the post req from frontend needs to match the strings here (e.g. 'type and 'message')
        # secret='nsEBcV7iNn1mNyzJnp3ThZDJQts'
        store_id = args['storeId']
        invoice_id = args['invoiceId']
        return {
            'resultStatus': 'SUCCESS',
            'message': "Invoice Settled Handler: " + store_id + " | " + invoice_id
        }

