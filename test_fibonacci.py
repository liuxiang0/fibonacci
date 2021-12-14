"""Test_Fibonacci.py"""

from fibonacci import Fibonacci, fibo_number, fibo_index, fibo_yield
from fibonacci import fibo_logical, fibo_iteral, fibo_matrix, fibo_lambda
from fibonacci import fibo_between

num = 20
func_list = (fibo_number, fibo_logical,fibo_iteral,fibo_index,fibo_matrix, fibo_lambda) #fibo_yield
for f in func_list:
    print('第{0}个Fibonacci数: {1} by {2}'.format(num, f(num), f.__name__))

fib = Fibonacci(num)
print('前{0}个Fibonacci数: {1} by {2}'.format(num, list(fib), 'Fibonacci'))
maxN = 2000
fib = Fibonacci(maxN, index=False)
print('不超过{0}的Fibonacci数: {1} by {2}'.format(maxN, list(fib), 'Fibonacci'))


fib = fibo_yield(num)
print('前{0}个Fibonacci数: {1} by {2}'.format(num, list(fib), fib.__name__))
fib = fibo_yield(num, 1,3)
print('最初两个数为1,3，前{0}个Fibonacci数: {1} by {2}'.format(num, list(fib), fib.__name__))


fib = fibo_between(num-10, num)
print('第{0}~{1}个Fibonacci数: {2} by {3}'.format(num-10, num, list(fib), 'fibo_between'))

# 大数测试
bigN = 2000
func = {fibo_number, fibo_index}  # 单个Fibonacci 数
for f in func:
    print('第{0}个Fibonacci数: {1} by {2}'.format(bigN, f(bigN), f.__name__))

#Fibonacci, 