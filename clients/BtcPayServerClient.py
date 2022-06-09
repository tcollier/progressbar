import os
import pickle

class BtcPayServerClient:

    def __init__(self):
        f = open("btcpayclient.creds", "rb")
        self.client = pickle.load(f)
        self.server_url = os.environ['SERVER_URL']

    def create_invoice(self):
        invoice = self.client.create_invoice({"price": 20, "currency": "SATS",
                                    "notificationURL": self.server_url + "/btcPay/invoiceCreated",
                                    "redirectURL": self.server_url + "/btcPay/invoiceSettled",
                                    "closeURL": self.server_url + "/btcPay/invoiceClosed",
                                    "orderId": "a", "itemDesc": "This is our item description",
                                    "physical": True})
        return invoice["url"]
