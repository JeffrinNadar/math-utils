# Functions for math

def factorial(n):
  if n < 0:
    raise ValueError("No Negative Numbers")

  if n == 0:
    return 1

  return n * factorial(n - 1)

def is_prime(n):
  if n < 2:
    return False

  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False

  return True