import requests

url = 'https://loomischaffee.org'

r = requests.get(url)

print(r.text)

