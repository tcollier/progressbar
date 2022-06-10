import os
import pickle

class BtcPayServerClient:

    def __init__(self):
        f = open("btcpayclient.creds", "rb")
        self.client = pickle.load(f)
        self.server_url = "https://btcpp-progress-bar.herokuapp.com"

    def create_invoice(self):
        item_id = "ALOHUSTMEA3HAKO72MLSWX3I"
        invoice = self.client.create_invoice({"price": 20, "currency": "SATS",
                                    "notificationURL": self.server_url + "/btcPay/invoiceSettled?itemId=" + item_id,
                                    "redirectURL": self.server_url + "/btcPay/invoiceCreated",
                                    "closeURL": self.server_url + "/btcPay/invoiceClosed",
                                    "itemId": item_id, "itemDesc": "This is our item description",
                                    "physical": True})
        return invoice["url"]
