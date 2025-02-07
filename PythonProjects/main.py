import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c5a19dfe5e149215312b629504b869e7'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 15
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''pokemon_id = response_create.json()['id']
print (pokemon_id)'''


body_change = {
    "pokemon_id": "219931",
    "name": "Пчеломах",
    "photo_id": 15
}

'''response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''


body_catch = {
    "pokemon_id": "219931"
}

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)