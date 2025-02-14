import pytest
from your_package_name.calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0.1, 0.2) == pytest.approx(0.3)

def test_subtract(calc):
    assert calc.subtract(5, 3) == 2
    assert calc.subtract(1, 1) == 0
    assert calc.subtract(0.3, 0.1) == pytest.approx(0.2)

def test_multiply(calc):
    assert calc.multiply(2, 3) == 6
    assert calc.multiply(-2, 3) == -6
    assert calc.multiply(0.1, 0.2) == pytest.approx(0.02)

def test_divide(calc):
    assert calc.divide(6, 2) == 3.0
    assert calc.divide(5, 2) == 2.5
    assert calc.divide(-6, 2) == -3.0
    
    with pytest.raises(ZeroDivisionError):
        calc.divide(5, 0)

def test_power(calc):
    assert calc.power(2, 3) == 8
    assert calc.power(2, 0) == 1
    assert calc.power(2, -1) == 0.5

def test_square_root(calc):
    assert calc.square_root(4) == 2.0
    assert calc.square_root(2) == pytest.approx(1.4142135623730951)
    
    with pytest.raises(ValueError):
        calc.square_root(-1)

def test_last_result(calc):
    calc.add(2, 3)
    assert calc.last_result == 5
    
    calc.multiply(4, 5)
    assert calc.last_result == 20 