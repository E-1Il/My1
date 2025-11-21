# tests/test_safe_division.py
import pytest
from safe_division import safe_division

def test_divides_positive_numbers():
    assert safe_division(10, 2) == 5

def test_divides_negative_numbers():
    assert safe_division(-9, 3) == -3
    assert safe_division(9, -3) == -3
    assert safe_division(-9, -3) == 3

def test_divides_floats():
    assert safe_division(7.5, 2.5) == 3.0

def test_zero_numerator():
    assert safe_division(0, 5) == 0

def test_divide_by_zero_returns_none(capfd):
    result = safe_division(5, 0)
    assert result is None
    # 檢查是否有正確的錯誤訊息輸出
    out, _ = capfd.readouterr()
    assert "錯誤：除數不能為零" in out

@pytest.mark.parametrize("a,b,expected", [
    (10, 5, 2),
    (1, 4, 0.25),
    (-6, 2, -3),
    (0, 1, 0),
])
def test_parameterized_cases(a, b, expected):
    assert safe_division(a, b) == expected
