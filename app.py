from flask import Flask, send_from_directory
from flask_restful import Api
from flask_cors import CORS  # comment this on deployment
from api.HelloApiHandler import HelloApiHandler
from api.InvoiceSettledHandler import InvoiceSettledHandler
from api.CocktailsMenuHandler import CocktailsMenuHandler
from api.CreateInvoiceHandler import CreateInvoiceHandler

app = Flask(__name__, static_url_path='', static_folder='frontend/build')
CORS(app)  # comment this on deployment
api = Api(app)


@app.route("/", defaults={'path': ''})
def serve(path):
    return send_from_directory(app.static_folder, 'index.html')


api.add_resource(HelloApiHandler, '/flask/hello')
api.add_resource(InvoiceSettledHandler, '/btcPay/invoiceSettled')
api.add_resource(CocktailsMenuHandler, '/cocktails')
api.add_resource(CreateInvoiceHandler, '/btcPay/createInvoice')

