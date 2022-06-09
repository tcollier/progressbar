from flask_restful import Resource


class InvoiceCreatedHandler(Resource):
    def get(self):
        return {
            'resultStatus': 'SUCCESS',
            'message': "Invoice was created"
        }

    def post(self):
        print(self)

