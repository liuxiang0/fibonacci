#!/usr/bin/python3
# -*- coding = utf-8 -*-
"""
Fibonacci: 最经典算法，用Python实现，递归、迭代多种方法体现
下面给出了多种实现fibonacci（n）的方法，全部是用Python语句实现，在Python3.6.4测试通过。
Author: Liu Xiang
Email : liuxiangxyd@163.com

"""

class FibMax(object):
    '''定义斐波那契数列类 FibMax(max), 有上界的迭代类，获得不超过max的所有fibonacci数'''

    def __init__(self, max):
        '''
        :param max: int, 不超过max
        '''
        self.max = max

    def __iter__(self):
        '''头两个缺省初值为 0, 1, 返回自己'''
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        '''迭代器中得到下一个 Fibonacci 数'''
        first = self.a  # 为了不漏掉第一个 0
        if first <= self.max:
            self.a, self.b = self.b, self.a + self.b
            return first
        else:
            raise StopIteration


if __name__ == '__main__':
    # 主要的区别就是利用了Python提供的默认参数和三元操作符，从而把代码简化至一行
    # 一条语句搞定：fib = lambda n, x=0, y=1: x if not n else fib(n-1, y, x+y)
    # 测试多种方法得到的 Fibonacci数，给定序列数n，得到第n个Fibonacci数。测试通过OK

    # *** 测试最大值 ***
    fib = FibMax(987)
    print(type(fib), list(fib))
    for f in fib:    # 为什么做了list后，fib没有变成了空集？
        print(f)    
