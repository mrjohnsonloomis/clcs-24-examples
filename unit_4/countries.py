import requests
import matplotlib.pyplot as plt
names = []
name = ''
pop = []
area = []
lat = []

while name != 'STOP':
    name = input('Which country would you like to follow? (enter STOP to stop): ')
    if name != 'STOP': names.append(name) 

for country in names:
    url = f'https://restcountries.com/v3.1/name/{country}'
    r = requests.get(url)
    data = r.json()
    pop.append(int(data[0]['population']))
    lat.append(float(data[0]['latlng'][0]))
    area.append(int(data[0]['area']))

area = [i / 1000 for i in area]
plt.scatter(pop, lat, s=area)
plt.show()

