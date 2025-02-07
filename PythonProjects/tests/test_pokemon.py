import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c5a19dfe5e149215312b629504b869e7'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = "18195"

def test_status_code():
    response = requests.get(url= f'{URL}/trainers',headers=HEADER)
    assert response.status_code == 200

def test_name_trainers():
    response_get = requests.get(url= f'{URL}/trainers',headers=HEADER , params = {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]['trainer_name'] == 'Kudryash'

 


    