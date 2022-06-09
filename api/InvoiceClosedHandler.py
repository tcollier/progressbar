from flask_restful import Resource


class InvoiceClosedHandler(Resource):
    def get(self):
        return {
            'resultStatus': 'SUCCESS',
            'message': "Invoice was closed"
        }

    def post(self):
        print(self)

