"""Test_Fibonacci.py"""

from fibonacci import Fibonacci

fib = Fibonacci(100, 3,10)

f = list(fib)
b = [x %3 for x in f]

print(b)
