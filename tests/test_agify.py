import requests


name = "lyserius"

URL = "https://api.agify.io?name=" + name

r = requests.get(url=URL)

data = r.json()

for key, value in data.items():
    print(f'{key}: {value}')

name = data['name']
age = data['age']
print(f'\n\n {name}, your age is {age} accoring to the agify api.')