import requests

url = 'https://www.google.com/'

r = requests.get(url)

print(r.text)

