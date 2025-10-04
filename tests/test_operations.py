import pytest
from math_utils.operations import factorial, is_prime

def test_factorial():
  assert factorial(0) == 1
  assert factorial(5) == 120
  with pytest.raises(ValueError):
    factorial(-1)

def test_is_prime():
  assert is_prime(2) is True
  assert is_prime(4) is False
  assert is_prime(17) is True