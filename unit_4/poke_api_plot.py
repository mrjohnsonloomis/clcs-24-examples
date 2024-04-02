import requests
import matplotlib.pyplot as plt

name = input('What pokemon do you want? : ')
response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}')


pokemon_info = response.json()

name = pokemon_info['name']
weight = pokemon_info['weight']
types = [t['type']['name'] for t in pokemon_info['types']]
abilities = [a['ability']['name'] for a in pokemon_info['abilities']]

#This is a dictionary comprehension. We haven't covered these yet.
stats = {s['stat']['name']: s['base_stat'] for s in pokemon_info['stats']}

print(f"Name: {name}")
print(f"Weight: {weight}")
print(f"Types: {', '.join(types)}")
print(f"Abilities: {', '.join(abilities)}")
print("Base Stats:")
for stat, value in stats.items():
    print(f"  {stat}: {value}")

# Plotting the base stats
plt.figure(figsize=(10, 6))
plt.bar(stats.keys(), stats.values())
plt.title(f"{name.capitalize()}'s Base Stats")
plt.xlabel('Stats')
plt.ylabel('Value')
plt.show()

