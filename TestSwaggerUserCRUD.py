import requests
import unittest
import json

class Swaggeruser(unittest.TestCase):
    def create(self):
        body = '{"id": 1, "username": "Merce", "firstName": "string","lastName": "string", "mail": "string", "password": "string", "phone": "string", "userStatus": 0}'
        body_json = json.loads(body)
        r = requests.post('https://petstore.swagger.io/v2/user', json=body_json)
        print(r.status_code)
    def test_a_create(self):
        self.create()
    def read(self):
        r = requests.get('https://petstore.swagger.io/v2/user/Merce')
        print(r.status_code)
    def test_b_read(self):
        self.read()
    def delete(self):
        r = requests.delete('https://petstore.swagger.io/v2/user/Merce')
        print(r.status_code)
    def test_c_delete(self):
        self.delete()

if __name__ == '__main__':
    unittest.main()