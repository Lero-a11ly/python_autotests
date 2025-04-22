import requests
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '9165b4d054a649352dfb927c9d65c047'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}


body_create = {
    
    "name": "Тралалейло тралала",
    "photo_id": 38
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)

print(response_create.text)

message = response_create.json()['message']
print(message)

body_change = {
     "pokemon_id": "298118",
    "name": "Пеппи Грош",
    "photo_id": 111
}

response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change ) 

print(response_change.text)

body_catch = {
    "pokemon_id": "298084"
}

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch ) 

print(response_catch.text)


