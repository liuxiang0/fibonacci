#!/usr/bin/python3
# -*- coding = utf-8 -*-
"""Fibonacci:用Python实现，递归、迭代多种方法体现
下面给出了多种实现fibonacci（n）的方法，全部是用Python语句实现，在Python3.6.4测试通过：
"""


def fibo_recursive(n):
    """
    # fibo_recursive(n): 要求很简单，输入n，输出第n个Fibonacci数，n为正整数。
    # algorithm: 递归算法recursive，耗资源比较大
    """
    if n == 0:
        return 0
    else:
        return (1 if n < 2 else fibo_recursive(n-1) + fibo_recursive(n-2))


def fibo_while(n):
    """
    # fibo_while(n): 非常简单的while循环方法，充分利用Python的三元操作符。
    # simple swap method: a, b, n = b, a+b, n-1
    """
    a, b = 0, 1
    while (n):
        a, b, n = b, a+b, n-1

    return a


def fibo_logical(n):
    """
    # fibo_logical(n): 递归迭代配合bool操作。
    # True = 1, False = 0, verify int(True) == 1, int(False) == 0
    """
    if n == 0:
        return 0
    else:
        return int(1 and n < 2) or fibo_logical(n-1) + fibo_logical(n-2)


def fibo_iteral(n):
    """
    # fibo_iteral(n): 定义递归‘迭代’函数。
    # using iterating method
    """
    def fibo_iter(n, x, y):
        if n == 0:
            return x
        else:
            return fibo_iter(n-1, y, x+y)

    return fibo_iter(n, 0, 1)


def fibo_lambda(n):
    """
    # fibo_lambda(n): 最精简的一条语句定义递归函数，三元操作符和递归结合。
    # using lambda and bool variable
    """
    __f = lambda n, x=0, y=1: x if not n else __f(n-1, y, x+y)
    return (__f(n))

if __name__ == '__main__':
    # 主要的区别就是利用了Python提供的默认参数和三元操作符，从而把代码简化至一行
    # 一条语句搞定：fib = lambda n, x=0, y=1: x if not n else fib(n-1, y, x+y)
    # 测试多种方法得到的 Fibonacci数，给定序列数n，得到第n个Fibonacci数。测试通过OK

    for i in range(15):
        print("Recursive=", fibo_recursive(i), "While=", fibo_while(i),
              "Logical=", fibo_logical(i), "Iteral=", fibo_iteral(i),
              "Lambda=", fibo_lambda(i))
    '''
    for i in range(15):
        print("Index=", i, "Recursive=", fibo_recursive(i),
              "While=", fibo_while(i), "Logical=", fibo_logical(i),
              "Iteral=", fibo_iteral(i), "Lambda=", fibo_lambda(i))'''
