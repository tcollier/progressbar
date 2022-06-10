import os

import dotsi
from square.client import Client

from clients.ClientUtils import *

LOCATION_ID = "LCRMPRZ047M9A"
CLIENT_ACCESS_TOKEN = "EAAAFFmvScsBx09oQgGC8O7utMsQF1FUvVfLx-RexkCV1wGbJMajAED1oPyJ-Gk2"

class MenuItem:
    def __init__(self, client, obj):
        self.client = client

        item_data = obj.item_data
        self.name = item_data.name
        self.image_ids = item_data.image_ids

        variation = item_data.variations[0]
        self.id = obj.id
        self.variation_id = variation.id
        self.price = variation.item_variation_data.price_money.amount

    def imageURL(self):
        return self.client.getImageURL(self.image_ids[0])

    def toJSON(self):
        return {
            "id": self.id,
            "variation_id": self.variation_id,
            "name": self.name,
            "price": self.price,
            "imageURL": self.imageURL()
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
            return [MenuItem(self, dotsi.Dict(rawObj)) for rawObj in result.body['objects'] if rawObj['type'] == 'ITEM']

        elif result.is_error():
            for error in result.errors:
                print(error['category'])
                print(error['code'])
                print(error['detail'])

    def getItem(self, itemId: str) -> MenuItem:
        result = self.client.catalog.retrieve_catalog_object(object_id = itemId)

        if result.is_success():
            rawObj = dotsi.Dict(result.body['object'])
            return MenuItem(self, rawObj)
            

    def getImageURL(self, imageId: str) -> str: 
        result = self.client.catalog.retrieve_catalog_object(object_id=imageId)
        obj = dotsi.Dict(result.body)
        return obj.object.image_data.url

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

