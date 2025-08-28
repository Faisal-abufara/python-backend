import pytest
from RealTest import AddThemNumbers, SubtractNumbers, IsEven

def test_AddThemNumbers_valid():
    assert AddThemNumbers(2, 3) == 5
    assert AddThemNumbers(2.5, 3.5) == 6.0

def test_AddThemNumbers_invalid():
    with pytest.raises(TypeError):
        AddThemNumbers("2", 3)
    with pytest.raises(TypeError):
        AddThemNumbers(2, "3")
    with pytest.raises(TypeError):
        AddThemNumbers("a", "b")

def test_SubtractNumbers():
    assert SubtractNumbers(5, 3) == 2
    assert SubtractNumbers(3, 5) == -2
    assert SubtractNumbers(5.5, 2.5) == 3.0

def test_IsEven_valid():
    assert IsEven(2) is True
    assert IsEven(3) is False
    assert IsEven(4.0) is True
    assert IsEven(5.0) is False

def test_IsEven_invalid():
    with pytest.raises(TypeError):
        IsEven("10")
    with pytest.raises(TypeError):
        IsEven(None)
