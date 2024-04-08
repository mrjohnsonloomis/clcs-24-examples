import requests

url = 'http://api.balldontlie.io/v1/players/?search={name}'
api_key = #your key here
header = {'Authorization': api_key}

r = requests.get(url, headers=header)

data = r.json()
print(data)
