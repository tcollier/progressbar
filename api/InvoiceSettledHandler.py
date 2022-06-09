from flask_restful import Api, Resource, reqparse

class InvoiceSettledHandler(Resource):
    def get(self):
        return {
            'resultStatus': 'SUCCESS',
            'message': "Invoice settled!"
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

