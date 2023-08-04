import requests
import unittest
import json

class Swaggerpet(unittest.TestCase):
    def create(self):
        body = '{"id": 666, "category": {"id": 1, "name": "good"}, "name": "Satana", "photoUrls": ["good"],"tags": [{"id": 1, "name": "good"}], "status": "Sold"}'
        body_json = json.loads(body)
        r = requests.post('https://petstore.swagger.io/v2/pet', json=body_json)
        print(r.status_code)
    def test_a_create(self):
        self.create()
    def read(self):
        r = requests.get('https://petstore.swagger.io/v2/pet/666')
        print(r.status_code)
    def test_b_read(self):
        self.read()
    def delete(self):
        r = requests.delete('https://petstore.swagger.io/v2/pet/666')
        print(r.status_code)
    def test_c_delete(self):
        self.delete()

if __name__ == '__main__':
    unittest.main()