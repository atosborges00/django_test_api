from webbrowser import get
import requests

# endpoint = 'https://httpbin.org/status/200/'
# endpoint = 'https://httpbin.org/anything'
endpoint = "http://localhost:8000/api/"

get_reponse = requests.get(endpoint, params={"abc": 123}, json={"query": "Hello world"})

# print(get_reponse.text)
# print(get_reponse.headers)
print(get_reponse.json())
# print(get_reponse.status_code)
