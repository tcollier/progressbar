from btcpay import BTCPayClient
import pickle

def main():
    f = open("btcpayclient.creds", "rb")
    client = pickle.load(f)
    new_invoice = client.create_invoice({"price": 20, "currency": "SATS", "notificationURL": "https://btcpp-progress-bar.herokuapp.com/webhooks/purchasePaid", "redirectURL": "https://btcpp-progress-bar.herokuapp.com/webhooks/purchaseSuccess", "closeURL": "https://btcpp-progress-bar.herokuapp.com/webhooks/purchaseAborted", "orderId": "a", "itemDesc": "This is our item description", "physical": True})
    
    #print(new_invoice['url'])
    #print(new_invoice['paymentCodes']['BTC_LightningLike']['BOLT11'])


if __name__ == "__main__":
    main()
