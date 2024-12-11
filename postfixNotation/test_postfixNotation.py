import pytest
from postfix import postfixNotation


def test_simple_addition():
    tokens = ["2", "3", "+"] # 2 + 3 
    assert postfixNotation(tokens) == 5

def test_multiplication_and_addition():
    tokens = ["2", "3", "*", "4", "+"] # 2 * 3 + 4 
    assert postfixNotation(tokens) == 10


def test_division_and_subtraction():
    tokens = ["10", "2", "/", "3", "-"] # 10 / 2 - 3 
    assert postfixNotation(tokens) == 2


def test_complex_expression_with_negatives():
    tokens = ["5", "-3", "*", "2", "+"] # (5 * -3) + 2
    assert postfixNotation(tokens) == -13


def test_single_operand():
    tokens = ["42"]
    assert postfixNotation(tokens) == 42


def test_division_by_zero():
    tokens = ["4", "0", "/"]
    with pytest.raises(ZeroDivisionError):
        postfixNotation(tokens)

def test_complex_expression():
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"] # ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    assert postfixNotation(tokens) == 22

def test_empty_input():
    tokens = []
    with pytest.raises(IndexError): 
        postfixNotation(tokens)


def test_float_division_as_int():
    tokens = ["10", "3", "/"] # 10 / 3 
    assert postfixNotation(tokens) == 3  

    