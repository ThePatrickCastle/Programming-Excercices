import pytest
from cumple import cumple

def test_basic_case_1():
    c = [1, 2, 1, 3, 2]
    d = 3
    m = 2
    assert cumple(c, d, m) == 2

def test_basic_case_2():
    c = [4, 1, 2, 1, 3, 2]
    d = 5
    m = 2
    assert cumple(c, d, m) == 2

def test_single_element_valid():
    c = [4]
    d = 4
    m = 1
    assert cumple(c, d, m) == 1

def test_single_element_invalid():
    c = [4]
    d = 3
    m = 1
    assert cumple(c, d, m) == 0

def test_no_valid_segments():
    c = [1, 1, 1, 1, 1]
    d = 10
    m = 2
    assert cumple(c, d, m) == 0

def test_multiple_valid_segments():
    c = [2, 2, 2, 2, 2]
    d = 4
    m = 2
    assert cumple(c, d, m) == 4

def test_segment_at_end():
    c = [1, 2, 1, 3, 2, 2, 1]
    d = 3
    m = 2
    assert cumple(c, d, m) == 3

def test_large_input():
    c = [1] * 1000000
    d = 2
    m = 2
    assert cumple(c, d, m) == 999999

def test_no_segment_possible():
    c = [3, 2, 1]
    d = 10
    m = 2
    assert cumple(c, d, m) == 0

def test_large_numbers():
    c = [1000, 2000, 3000, 4000, 5000]
    d = 3000
    m = 1
    assert cumple(c, d, m) == 1

def test_exact_match_whole_bar():
    c = [1, 2, 3]
    d = 6
    m = 3
    assert cumple(c, d, m) == 1

def test_basic_case_last():
    c = [2,2,1,3,2]
    d = 4
    m = 2
    assert cumple(c, d, m) == 2