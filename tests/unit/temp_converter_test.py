import pytest
from . import convertCtoF

def test_convertCtoF():
    assert convertCtoF(21) == 69.8
