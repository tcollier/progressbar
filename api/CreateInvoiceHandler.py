from flask_restful import Resource
from flask import redirect, url_for

from clients.BtcPayServerClient import BtcPayServerClient


class CreateInvoiceHandler(Resource):
    def get(self):
        invoice_url = BtcPayServerClient().create_invoice()
        return redirect(invoice_url)

    def post(self):
        print(self)

