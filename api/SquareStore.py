from datetime import date, timedelta 
import uuid

from square.client import Client as SquareClient

LOCATION_ID = "LCRMPRZ047M9A"

def _uuidStr() -> str:
  return str(uuid.uuid4())

def _todayStr() -> str:
  return str(date.today())

def _tomorrowStr() -> str:
  return str(date.today() + timedelta(days=1))

def _createOrder(squareClient: SquareClient, itemVariationId) -> str:
  idempotencyKey = _uuidStr()

  result = squareClient.orders.create_order(
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
                          "expires_at": _todayStr(),
                          "pickup_at": _tomorrowStr(),
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
    result.body.id


def _createPayment(squareClient: SquareClient, moneyAmount: int, orderId: str) -> str:
    idempotencyKey =  _uuidStr()
    result = client.payments.create_payment(
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
      result.body.id

def createOrder(squareClient: SquareClient, itemVariation) -> str:
  orderId = _createOrder(squareClient, itemVariation.item_id)
  paymentId = _createPayment(squareClient, moneyAmount, orderId)
