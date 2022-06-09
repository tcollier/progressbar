import os

import dotsi
from square.client import Client

from clients.ClientUtils import *

LOCATION_ID = "LCRMPRZ047M9A"
CLIENT_ACCESS_TOKEN = "EAAAFFmvScsBx09oQgGC8O7utMsQF1FUvVfLx-RexkCV1wGbJMajAED1oPyJ-Gk2"

class MenuItem:
    def __init__(self, rawObj):
        obj = dotsi.Dict(rawObj)
        self.name = obj.item_data.name

        variation = obj.item_data.variations[0]

        self.id = variation.id
        self.price = variation.item_variation_data.price_money.amount

    def toJSON(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
        }




class SquareupClient:
    def __init__(self):
        self.client = Client(
            access_token=CLIENT_ACCESS_TOKEN,
            environment='production'
        )

    def getMenu(self):
        result = self.client.catalog.list_catalog()

        if result.is_success():

            return [MenuItem(rawObj) for rawObj in result.body['objects'] if rawObj['type'] == 'ITEM']

        elif result.is_error():
            for error in result.errors:
                print(error['category'])
                print(error['code'])
                print(error['detail'])

    def _createOrder(self, itemVariationId) -> str:
        idempotencyKey = uuidStr()

        result = self.client.orders.create_order(
            body={
                "order": {
                    "location_id": LOCATION_ID,
                    "line_items": [
                        {
                            "quantity": "1",
                            "catalog_object_id": itemVariationId, 
                        }
                    ],
                    "fulfillments": [
                        {
                            "type": "PICKUP",
                            "state": "PROPOSED",
                            "pickup_details": {
                                "recipient": {
                                    "display_name": "Anon Y. Mouse"
                                },
                                "expires_at": tomorrowStr(),
                                "pickup_at": tomorrowStr(),
                                "is_curbside_pickup": False
                            }
                        }
                    ]
                },
                "idempotency_key": idempotencyKey,
            }
        )
        if result.is_error():
            print(f"ERRORS!: ${result.errors}")
        else:
            # return the order id
            return dotsi.Dict(result.body).order.id


    def _createPayment(self, moneyAmount: int, orderId: str) -> str:
        idempotencyKey = uuidStr()

        result = self.client.payments.create_payment(
            body={
                "source_id": "EXTERNAL",
                "idempotency_key": idempotencyKey,
                "amount_money": {
                    "amount": moneyAmount,
                    "currency": "USD"
                },
                "order_id": orderId,
                "location_id": LOCATION_ID,
                "external_details": {
                    "type": "CRYPTO",
                    "source": "lightning"
                }
            }
        )

        if result.is_error():
            print(f"ERRORS!: ${result.errors}")
        else:
            # return the order id
            return dotsi.Dict(result.body).payment.id

    def createOrder(self, itemVariation) -> str:
        orderId = self._createOrder(itemVariation.id)
        paymentId = self._createPayment(itemVariation.price, orderId)
        return paymentId

