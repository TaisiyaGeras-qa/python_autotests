import requests

URL ="https://api.pokemonbattle.ru/v2"
TOKEN ="TRAINER_TOKEN"
HEADER ={"Content-Type" : "application/json", "trainer_token": TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "USER_LOGIN",
    "password": "USER_PASSWORD",
    "password_re": "USER_PASSWORD"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Ирчи",
    "photo_id": 898
}
body_change_name = {
    "pokemon_id": "372015",
    "name": "Пирожок",
    "photo_id": 898
}
body_add_pokeball = {
    "pokemon_id": "372015"
}

body_change_trainers_name = {
    "name": "AsIs",
    "city": "Москва"
}

'''response = requests.post(url = f"{URL}/trainers/reg", headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url=f"{URL}/trainers/confirm_email", headers=HEADER, json = body_confirmation)
print(response_confirmation.text)'''

'''response_create = requests.post(url=f"{URL}/pokemons", headers=HEADER, json = body_create)
print(response_create.text)'''

'''response_change_name = requests.put(url=f"{URL}/pokemons", headers=HEADER, json = body_change_name)
print(response_change_name.text)'''

'''response_add_pokeball = requests.post(url=f"{URL}/trainers/add_pokeball", headers=HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)'''

response_change_trainers_name = requests.put(url=f"{URL}/trainers", headers=HEADER, json = body_change_trainers_name)
print(response_change_trainers_name.text)
