import requests
import matplotlib.pyplot as plt

url = f'https://restcountries.com/v3.1/name/brazil'
r = requests.get(url)
data = r.json()

print(data[0]['area'])