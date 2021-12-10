#!/usr/bin/python3
# -*- coding = utf-8 -*-
"""
Fibonacci: 最经典算法，用Python实现，递归、迭代多种方法体现
下面给出了多种实现fibonacci（n）的方法，全部是用Python语句实现，在Python3.6.4测试通过。
Author: Liu Xiang
Email : liuxiangxyd@163.com

"""

class Fibonacci(object):
    '''定义斐波那契数列类 Fibonacci(n,a=0,b=1), 迭代类'''

    def __init__(self, n=2, a=0, b=1) -> None:
        '''
        :param n: int, 生成数列的个数为指定的整数 n
        '''
        self.n = n
        # 头两个缺省初值为 0,1，可以修改。
        self.a = a
        self.b = b
        # 保存当前数列的位置，记录当前位置下标
        self.curpos = 0
        # 记录初始值
        self._first = a
        self._second = b


    def __iter__(self):
        '''返回自己就行'''
        return self

    def __next__(self):
        ''' 迭代器中得到下一个 Fibonacci 数 '''
        if self.curpos < self.n:
            self.a, self.b = self.b, self.a + self.b
            self.curpos += 1
            return self.a
        else:
            raise StopIteration

    #作为装饰器，将类方法转换为类属性（只读）
    #property重新实现一个属性的setter和getter方法
    @property
    def first(self):
        return self._first

    @first.setter
    def first(self, first):
        self._first = first

    @property
    def second(self):
        return self._second

    @second.setter
    def second(self, second):
        self._second = second

    #类方法，只能是类属性，不能使用实例属性，必须使用类的对象作为第一个参数
    @classmethod
    def list(cls):
        return list(cls)

    #静态方法，不强制要求传递参数
    #@staticmethod

    @staticmethod
    def lamb(self, n):
        __f = lambda n, x=self._first, y=self._second : x if not n else __f(n-1, y, x+y)
        return (__f(n))


def fib_while(n):
    """推荐该算法
    # fib_while(n): 非常简单的while循环方法，充分利用Python的三元操作符。
    # simple swap method: a, b, n = b, a+b, n-1
    # 测试 500 以上没有问题。其它递归肯定慢。
    """
    assert n >= 0, 'n为自然数'
    a, b = 0, 1
    if n==0:
        return n   #yield a  # 第一个为 0
    while (n):
        a, b, n = b, a+b, n-1
        #yield a
    return a

def fibo_iteral(n):
    """推荐该算法，等同于 fib_while(n)
    # fibo_iteral(n): 递归迭代函数。
    # using iterating method
    """
    assert n >= 0, 'n为自然数'
    def fibo_iter(n, x, y):
        if n == 0:
            return x
        else:
            return fibo_iter(n-1, y, x+y)

    return fibo_iter(n, 0, 1)


def fibo_lambda(n):
    """推荐该算法，等同于 fibo_while(n)
    # fibo_lambda(n): 最精简的一条语句定义递归函数，三元操作符和递归结合。
    # using lambda and bool variable
    # 等价于一条语句 fib = lambda n, x=0, y=1: x if not n else fib(n-1,y,x+y)
    """
    assert n >= 0, 'n为自然数'
    __f = lambda n, x=0, y=1: x if not n else __f(n-1, y, x+y)
    return (__f(n))



def fibo_logical(n):
    """
    # fibo_logical(n): 递归迭代配合bool操作。
    # True = 1, False = 0, verify int(True) == 1, int(False) == 0
    # 不推荐
    """
    if n == 0:
        return 0
    else:
        return int(1 and n < 2) or fibo_logical(n-1) + fibo_logical(n-2)


def fibo_matrix(n):
    """矩阵方法: [f_n f_{n-1}] = [f_{n-1} f_{n-2}]*M =...
    = [f_1,f_0]*M^{n-1} , M=matrix[[1,1],[1,0]]
    Using numpy.dot(A,B)
    局限: n大于46，即出现溢出，得到负数；
    不推荐该算法。
    """
    import numpy as np

    M = [[1,1],[1,0]]
    E = [[1,0],[0,1]]
    F = [[1],[0]]

    assert n >= 0, 'n为自然数'
    if (n==0 or n==1):
        return n
    for _ in range(n-1):
        E = np.dot(E, M)
    #print(E)
    S = np.dot(E,F)
    return S[0][0]
    


if __name__ == '__main__':
    # 主要的区别就是利用了Python提供的默认参数和三元操作符，从而把代码简化至一行
    # 一条语句搞定：fib = lambda n, x=0, y=1: x if not n else fib(n-1, y, x+y)
    # 测试多种方法得到的 Fibonacci数，给定序列数n，得到第n个Fibonacci数。测试通过OK

    fib = 1
    num = 500
    while num < 520 and fib >0:
        fib = fibo_lambda(num)  #fibo_matrix(num)
        print(num, fib)
        num += 1

    '''fib = Fibonacci()
    fib = fib.fwhile(4)
    for f in fib:
        print(f)

    for i in range(15,30):
        print("{i}：Recursive={R} While={W} Logical={L} Iteral={T} Lambda={A}".format(i=i+1,
            R=fibo_recursive(i), W=fibo_while(i), L=fibo_logical(i), T=fibo_iteral(i), A=fibo_lambda(i)))
    
    for i in range(15):
        print("Index=", i, "Recursive=", fibo_recursive(i),
              "While=", fibo_while(i), "Logical=", fibo_logical(i),
              "Iteral=", fibo_iteral(i), "Lambda=", fibo_lambda(i))
    '''