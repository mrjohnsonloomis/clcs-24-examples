import requests

url = 'http://api.balldontlie.io/v1/players/?search={name}'
api_key = '3212288b-91af-408c-8471-518cd5fca5e5'
header = {'Authorization': api_key}

r = requests.get(url, headers=header)

data = r.json()
print(data)
