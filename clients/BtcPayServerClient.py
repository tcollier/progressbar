import os
import pickle

class BtcPayServerClient:

    def __init__(self):
        f = open("btcpayclient.creds", "rb")
        self.client = pickle.load(f)
        self.server_url = os.environ['SERVER_URL']

    def create_invoice(self, item_id, item_price):
        invoice = self.client.create_invoice({"price": item_price, "currency": "SATS",
                                    "notificationURL": self.server_url + "/btcPay/invoiceSettled?itemId=" + item_id,
                                    "redirectURL": self.server_url + "/btcPay/invoiceCreated",
                                    "closeURL": self.server_url + "/btcPay/invoiceClosed",
                                    "orderId": item_id,
                                    "itemId": item_id, "itemDesc": "This is our item description",
                                    "physical": True})
        return invoice["url"]
