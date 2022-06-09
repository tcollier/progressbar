from btcpay import BTCPayClient
import pickle


class BtcPayServerClient:

    def __init__(self):
        f = open("btcpayclient.creds", "rb")
        self.client = pickle.load(f)

    def create_invoice(self):
        invoice = self.client.create_invoice({"price": 20, "currency": "SATS",
                                    "notificationURL": "https://btcpp-progress-bar.herokuapp.com/btcPay/invoiceCreated",
                                    "redirectURL": "https://btcpp-progress-bar.herokuapp.com/btcPay/invoiceSettled",
                                    "closeURL": "https://btcpp-progress-bar.herokuapp.com/btcPay/invoiceClosed",
                                    "orderId": "a", "itemDesc": "This is our item description",
                                    "physical": True})
        return invoice["url"]
