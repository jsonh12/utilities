import pytest
from utilities.temp_converter import convertCtoF

def test_convertCtoF():
    assert convertCtoF(21) == 69.8
