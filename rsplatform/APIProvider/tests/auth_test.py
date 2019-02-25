import requests
import unittest

def url(endpoint, url="http://0.0.0.0:5000"):
    url=os.popen(("docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' rsplatform_apiprovider_1")).read().split("\n")
    url+=":5000"
    print(url)
    return (url+endpoint).strip()

class AuthTest(unittest.TestCase):
    def test_connection(self, endpoint="/api/v1/register"):
        response = None
        response = requests.get(url(endpoint))
        self.assertFalse(response is None, msg="500 Internal Server Error.")
        print(response.status_code)
        print(response.json())

if __name__ == '__main__':
    unittest.main()
