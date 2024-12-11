import pytest

from saltos import saltos

def test_saltos1():
    arreglo1 = [1,2,3,4,5]
    assert saltos(arreglo1) == True

def test_saltos2():
    arreglo2 = [1,1,2,2]
    assert saltos(arreglo2) == True

def test_saltos3():
    arreglo3 = [3,2,1,0,4]
    assert saltos(arreglo3) == False

def test_saltos4():
    arreglo4 = [3, 3, 1, 2, 0, 1]
    assert saltos(arreglo4) == True

def test_saltos5():
    arreglo5 = [0]
    assert saltos(arreglo5) == True

def test_saltos6():
    arreglo6 = [1, 2, 0, 0, 1]
    assert saltos(arreglo6) == False

def test_saltos7():
    arreglo7 = [1, 2, 0, 1]
    assert saltos(arreglo7) == True

def test_saltos8():
    arreglo8 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1]
    assert saltos(arreglo8) == False

def test_saltos8():
    arreglo8 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
    assert saltos(arreglo8) == True

