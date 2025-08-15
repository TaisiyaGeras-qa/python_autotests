"Basic tests"
import requests
import pytest

URL ="https://api.pokemonbattle.ru/v2"
TOKEN ="TRAINER_TOKEN"
HEADER ={"Content-Type" : "application/json", "trainer_token": TOKEN}
TRAINER_ID = "41785"

def test_status_code():
    """
    TRF-23. [api][get][pokemons] Проверка статус-кода ответа покемонов
    """
    response = requests.get(url = f'{URL}/pokemons', params={'trainer_id' : TRAINER_ID}, timeout=2)
    assert response.status_code == 200, "Unexpected status-code"

def test_part_of_response():
    """
    TRF-24. [api][get][pokemons] Проверка имени покемона в ответе
    """
    response_get = requests.get(url = f'{URL}/pokemons', params={'trainer_id' : TRAINER_ID},
                                timeout=2)
    assert response_get.json()["data"][0]["name"] == "Ирчи", "Unexpected pokemon name"

def test_status_code_trainers():
    """
    TRF-25. [api][get][trainers] Проверяет, что GET запрос к /trainers возвращает статус 200
    """
    response_trainers = requests.get(url = f'{URL}/trainers', timeout=2)
    assert response_trainers.status_code == 200, "Unexpected trainer status-code"

def test_part_of_response_trainers():
    """
    TRF-26. [api][get][trainers] Проверка, что GET запрос к /trainers с trainer_id возвращает правильное имя тренера
    """
    response_get_trainers = requests.get(url = f'{URL}/trainers',
                                         params={'trainer_id' : TRAINER_ID}, timeout=2)
    assert response_get_trainers.json()["data"][0]["trainer_name"] == "AsIs", "Unexpected trainer name"

@pytest.mark.parametrize("key, value", [("name", "Ирчи"), ("trainer_id", TRAINER_ID), ("id", "372026")])
def test_parametrize(key, value):
    """
    TRF-27. [api][get][pokemons] Проверка соответствия ключ-значение
    """
    response_parametrize = requests.get(url = f'{URL}/pokemons',
                                        params={'trainer_id' : TRAINER_ID}, timeout=2)
    assert response_parametrize.json()["data"][0][key] == value, "Unexpected value for key"
