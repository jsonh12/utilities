import pytest
from temp_converter import convertCtoF

def test_convertCtoF():
    assert convertCtoF(265) == 4
