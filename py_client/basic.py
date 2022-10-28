from webbrowser import get
import requests

# endpoint = 'https://httpbin.org/status/200/'
# endpoint = 'https://httpbin.org/anything'
endpoint = "http://localhost:8000/"

get_reponse = requests.get(endpoint)

print(get_reponse.text)
print(get_reponse.status_code)
