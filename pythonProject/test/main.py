import requests
URL='https://api.pokemonbattle.ru/v2'
TOKEN='7b7bbef020651002b6708ba4debc2bdc'
HEADER={'Content-Type':'application/json', 'trainer_token':TOKEN}
body_registration={"trainer_token": TOKEN, "email": "user_email", "password": "user_password"}
body_confirmation={"trainer_token": TOKEN}
body_create={"name": "generate", "photo_id": -1}
body_name={"pokemon_id": "45586", "name": "POP", "photo_id": 2}
body_add_pokeball={"pokemon_id": "45586"}
'''response=requests.post(url = F'{URL}/trainers/reg', headers=HEADER, json=body_registration)
print(response.text)
response_confirmation=requests.post(url = F'{URL}/trainers/confirm_email', headers=HEADER, json=body_confirmation)
print(response_confirmation.text)'''
'''response_create=requests.post(url=f'{URL}/pokemons', headers=HEADER, json=body_create)
print(response_create.text)
pokemon_id=response_create.json()['id']['message']
print(pokemon_id)'''
'''response_name=requests.put(url=f'{URL}/pokemons', headers=HEADER, json=body_name)
print(response_name.text)
pokemon_id=response_name.json()['id']['message']
print(pokemon_id)'''
response_add_pokeball=requests.post(url=f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_add_pokeball)
print(response_add_pokeball.text)