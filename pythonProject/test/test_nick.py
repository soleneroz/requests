import requests
import pytest
URL='https://api.pokemonbattle.ru/v2'
TOKEN='user_token'
HEADER={'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID='6475'
POKEMON_ID='45586'
POKEMON_NAME='krov'
def test_status_code():
    response=requests.get(url=f'{URL}/pokemons', params={'trainer_id' : TRAINER_ID})
    assert response.status_code ==200
def test_part_of_response():
    response_get=requests.get(url=f'{URL}/pokemons', params={'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["name"]==POKEMON_NAME

@pytest.mark.parametrize('key,value',[('name', POKEMON_NAME),('trainer_id', TRAINER_ID),('id', POKEMON_ID)])
def test_parametrize(key,value):
    response_parametrize=requests.get(url=f'{URL}/pokemons', params={'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key]==value