from requests import get

def url(endpoint, url="http://127.0.0.1:5000"):
    return (url+endpoint).strip()


def register_test(endpoint="/auth/register"):
    response = get(url(endpoint))
    print(response.json())

register_test()
