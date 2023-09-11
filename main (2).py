def factorial_loop(n):
  result = 1
  for i in range(1, n + 1):
    result *= i
  return result


number = 5
factorial = factorial_loop(number)
print("Factorial of", number, "is", factorial)
