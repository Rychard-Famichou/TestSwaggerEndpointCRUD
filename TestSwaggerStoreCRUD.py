import requests
import unittest
import json

class Swaggerstore(unittest.TestCase):
    def create(self):
        body = '{"id": 1,"petId": 666,"quantity": 1,"shipDate": "2023-08-04T11:55:47.345Z","status": "placed","complete": true}'
        body_json = json.loads(body)
        r = requests.post('https://petstore.swagger.io/v2/store/order', json=body_json)
        print(r.status_code)
    def test_a_create(self):
        self.create()
    def read(self):
        r = requests.get('https://petstore.swagger.io/v2/store/order/1')
        print(r.status_code)
    def test_b_read(self):
        self.read()
    def delete(self):
        r = requests.delete('https://petstore.swagger.io/v2/store/order/1')
        print(r.status_code)
    def test_c_delete(self):
        self.delete()

if __name__ == '__main__':
    unittest.main()