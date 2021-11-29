import json
import requests
from random import randint

food_choice = input('Masukan nama makanan : ')
url = f'https://api.punkapi.com/v2/beers?food={food_choice}'
r = requests.get(url)
data = json.loads(r.text)

pie_list = []

for pie in data:
    name = pie['tagline']
    image = pie['image_url']
    boil = pie['boil_volume']

    pie_dict = {
        'Name': name,
        'Image': image,
        'Boil': boil
    }
    pie_list.append(pie_dict)


