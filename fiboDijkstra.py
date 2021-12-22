"""测试大数据的Fibonacci数
    目前发现的最好的算法: Dijkstra算法。300万都没有问题
    我已经不想再扩大了。
"""

from fibonacci import fibo_dijkstra,fibo_index,fibo_number

# 大数测试，寻找超大Fibonacci数
bigN = 1000000
func = {fibo_dijkstra}  # 单个Fibonacci 数fibo_index, fibo_number , 
for f in func:
    print('第{0}个Fibonacci数: {1} by {2}'.format(bigN, f(bigN), f.__name__))
