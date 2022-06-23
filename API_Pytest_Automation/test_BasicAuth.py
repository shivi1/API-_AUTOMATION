import requests
from requests.auth import HTTPBasicAuth

def test_basic_auth():
    response = requests.get("https://api.github.com/user", auth=HTTPBasicAuth('shivangi.move@gmail.com','Iamshivi@1'))
    print(response.text)
