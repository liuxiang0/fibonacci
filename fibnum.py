#!/usr/bin/python3
# -*- coding = utf-8 -*-
"""
Fibonacci: 最经典算法，用Python实现，递归、迭代多种方法体现
下面给出了多种实现fibonacci（n）的方法，全部是用Python语句实现，在Python3.6.4测试通过。
Author: Liu Xiang
Email : liuxiangxyd@163.com

"""

class FibNum(object):
    '''定义斐波那契数列类 FibNum(num), 初始为第0个，结尾为第num个，迭代类'''

    def __init__(self, num):
        '''
        :param num: int, 生成数列的个数为指定的整数 num+1
        '''
        self.num = num
        self.curpos = 0
        
    def __iter__(self):
        '''头两个缺省初值为 0, 1，返回自己'''
        self.a = 0
        self.b = 1
        return self

    def __next__(self):
        ''' 迭代器中得到下一个 Fibonacci 数 '''
        fib = self.a  # 为了不漏掉第0个数，与自然数统一
        if self.curpos <= self.num:
            self.a, self.b = self.b, self.a + self.b
            self.curpos += 1
            return fib  #self.a
        else:
            raise StopIteration
    
    #类方法，只能是类属性，不能使用实例属性，必须使用类的对象作为第一个参数
    @classmethod
    def list(cls):
        return list(cls)


if __name__ == '__main__':
    # 主要的区别就是利用了Python提供的默认参数和三元操作符，从而把代码简化至一行
    # 一条语句搞定：fib = lambda n, x=0, y=1: x if not n else fib(n-1, y, x+y)
    # 测试多种方法得到的 Fibonacci数，给定序列数n，得到第n个Fibonacci数。测试通过OK

    fib = FibNum(35)
    print(type(fib), list(fib))
    
    for f in fib:  # 为什么做了list后，fib变成了空集？
        print(f)
