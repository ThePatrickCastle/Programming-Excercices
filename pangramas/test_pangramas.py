# test_pangramas.py

import pytest
from pangramas import pangramas

def test_pangramas_es_pangrama():
    s = "Le gustaba cenar un exquisito sándwich de jamón con zumo de piña y vodka fría"
    result = pangramas(s)
    assert result == "Es Pangrama"

def test_pangramas_no_es_pangrama():
    s = "Esto no es un pangrama"
    result = pangramas(s)
    assert result == "No es pangrama"

def test_pangramas_1():
    s = "El viejo Señor Gómez pedía queso, kiwi y habas, pero le ha tocado un saxofón"
    result = pangramas(s)
    assert result == "Es Pangrama"

def test_pangramas_2():
    s = "Nada relevante"
    result = pangramas(s)
    assert result == "No es pangrama"

def test_pangramas_3():
    s = "El extraño whisky quemó como fuego la boca del joven López"
    result = pangramas(s)
    assert result == "Es Pangrama"

def test_pangramas_4():
    s = "Fidel exporta gazpacho, jamón, kiwi, viñas y buques"
    result = pangramas(s)
    assert result == "Es Pangrama"

def test_pangramas_todo_minusculas():
    s = "queda gazpacho, fibra, látex, jamón, kiwi y vias"
    result = pangramas(s)
    assert result == "No es pangrama"

def test_pangramas_todo_mayusculas():
    s = "EL VELOZ MURCIÉLAGO HINDÚ COMÍA FELIZ KIWI"
    result = pangramas(s)
    assert result == "No es pangrama" 

def test_pangramas_espacios():
    s = "                            "
    result = pangramas(s)
    assert result == "No es pangrama"
    
def random_caracteres():
    s = "¿?¡!@#$%^&*()_+*[]:;.,<>/|===--################ñ"
    result = pangramas(s)
    assert result == "No es pangrama"