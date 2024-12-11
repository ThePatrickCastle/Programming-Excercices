import pytest
from romanos import numerosRomanos

def test_romanToInt1():
    assert numerosRomanos("III") == 3
def test_romanToInt2():
    assert numerosRomanos("IV") == 4
def test_romanToInt3():
    assert numerosRomanos("IX") == 9
def test_romanToInt4():
    assert numerosRomanos("LVIII") == 58
def test_romanToInt5():
    assert numerosRomanos("MCMXCIV") == 1994
def test_romanToInt6():
    assert numerosRomanos("XL") == 40
def test_romanToInt7():
    assert numerosRomanos("XC") == 90
def test_romanToInt8():
    assert numerosRomanos("CD") == 400
def test_romanToInt9():
    assert numerosRomanos("CM") == 900
def test_romanToInt10():
    assert numerosRomanos("MMXXIII") == 2023

if __name__ == "__main__":
    pytest.main()