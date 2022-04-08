"""Test_Fibonacci.py"""

from fibonacci import Fibonacci, fibo_number, fibo_index, fibo_yield
from fibonacci import fibo_dijkstra
from fibonacci import fibo_logical, fibo_iteral, fibo_matrix, fibo_lambda
from fibonacci import fibo_between, fibo_perfect

num = 30

# 递归迭代方法，不能太大，不超过40
func_list = (fibo_logical, fibo_iteral, fibo_index, fibo_lambda)
for f in func_list:
    print('第{0}个Fibonacci数: {1} by {2}'.format(num, f(num), f.__name__))

# Python类方法（序号）
fib = Fibonacci(num)
print('前{0}个Fibonacci数: {1} by {2}'.format(num, list(fib), 'Fibonacci'))
# Python类方法（最大Fibonacci数）
maxN = 100000
fib = list(Fibonacci(maxN, index=False))
print('不超过{0}的Fibonacci数: {1} by {2}'.format(maxN, fib[-1], 'Fibonacci'))

num = 70
# 生成器方法（Fibonacci序列）
fib = fibo_yield(num)
print('前{0}个Fibonacci数: {1} by {2}'.format(num, list(fib), fib.__name__))
# 生成器方法（Lucas序列）
fib = fibo_yield(num, 2, 1)
print('最初两个数为1,3，前{0}个Lucas数: {1} by {2}'.format(num, list(fib), fib.__name__))

# 只截取一段Fibonacci数
fib = fibo_between(num-10, num)
print('第{0}~{1}个Fibonacci数: {2} by {3}'.format(num-10, num, list(fib), 'fibo_between'))

# 矩阵自乘方法,符号运算，非常大数据也没有问题, 超过10万变成了符号运算。
num = 100000
fib = fibo_matrix(num)
print('第{0}个Fibonacci数: {1} by {2}'.format(num, fib, fibo_matrix.__name__))


# 大数测试，寻找超大Fibonacci数
bigN = 5000
func = {fibo_number, fibo_index, fibo_dijkstra}  # 单个Fibonacci 数
for f in func:
    print('第{0}个Fibonacci数: {1} by {2}'.format(bigN, f(bigN), f.__name__))

## 特殊Fibonacci数，序号==数位之和 with (index == digit sum)
num = 10000
fibList = fibo_perfect(num)
print('特殊Fibonacci数（序号==其数位之和），序号<={0}, 个数={1}，列表{2}, by {3}'.format(num, len(fibList), fibList, fibo_perfect.__name__))

