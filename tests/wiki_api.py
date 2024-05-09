#https://en.wikipedia.org/w/rest.php/v1/search/page?q=earth&limit=1

import requests
import re

name = "sonic the hedgehog"

URL = "https://en.wikipedia.org/w/rest.php/v1/search/page?q=" + name + '&limit=1'

r = requests.get(url=URL)

data = r.json()

#for key, value in data.items():
#    print(f'{key}: {value}')

page = data['pages'][0]
title = page['title']
excerpt = page['excerpt']

s = f'{title}: {excerpt}'

# remove <span> references
pattern = re.compile(r"\<(.*?)\>")
s = re.sub(pattern, "", s)
print(s)

#print(f'\n\n {name}, your age is {age} accoring to the agify api.')