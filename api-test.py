import requests
url = 'http://127.0.0.1:5000/'
params = {'query': "This is really great movie"}
response = requests.get(url, params)
response.json()
print(response)
print(response.json())

