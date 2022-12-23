from .workalg import *
from .shortline import *


def test_empty():
    assert shortened_line(' ') == ' '

def test_line_classic():
    assert line_classic('a3b5') == 'aaabbbbb'

def test_shortened_line():
    assert shortened_line('aaabbb') == 'a3b3'

def test_check_digits():
    assert check_digits('123') == True

def test_digit_begin():
    assert digit_begin('1a56') == True

def test_digit_zero():
    assert digit_zero('100') == True