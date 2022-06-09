from flask_restful import Api, Resource, reqparse

class InvoiceSettledHandler(Resource):
    def get(self):
        return {
            'resultStatus': 'SUCCESS',
            'message': "Invoice settled handler"
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

