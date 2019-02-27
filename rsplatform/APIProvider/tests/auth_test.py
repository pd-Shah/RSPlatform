import requests
import unittest
import os

def url(endpoint, url="http://0.0.0.0:5000"):
    return (url+endpoint).strip()

class AuthTest(unittest.TestCase):
    def test_connection(self, endpoint="/api/v1/register"):
        response = None
        response = requests.get(url(endpoint))
        self.assertFalse(response is None, msg="500 Internal Server Error.")
        print(response.status_code)
        print(response.json())

# if __name__ == '__main__':
#     unittest.main()
