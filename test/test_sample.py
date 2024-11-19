import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from sample import addition  # Importe la fonction addition
from sample import substraction
from sample import multiplication

def test_addition():
    assert addition(10, 5) == 15


def test_subtraction():
    assert substraction(10, 5) == 5

def test_multiplication():
    assert multiplication(3, 4) == 12

