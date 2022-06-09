from square.client import Client
import os

class SquareupClient:

    def __init__(self):
        self.client = Client(
            access_token=os.environ['SQUARE_ACCESS_TOKEN'],
            environment='production'
        )

    def list_locations(self):
        result = self.client.locations.list_locations()

        if result.is_success():
            for location in result.body['locations']:
                print(f"{location['id']}")
                print(f"{location['name']}")
                print(f"{location['address']['address_line_1']}")
                print(f"{location['address']['locality']}")

        elif result.is_error():
            for error in result.errors:
                print(error['category'])
                print(error['code'])
                print(error['detail'])

    def list_catalog_items(self):
        result = self.client.catalog.list_catalog()

        if result.is_success():
            for object in result.body['objects']:
                if object['type'] == 'ITEM':
                    print(f"{object['item_data']['name']}")
                    print(f"{object['item_data']['variations'][0]['item_variation_data']['price_money']}")

        elif result.is_error():
            for error in result.errors:
                print(error['category'])
                print(error['code'])
                print(error['detail'])







