#!/usr/bin/python3
# -*- coding = utf-8 -*-
"""
Fibonacci: 最经典算法，用Python实现，递归、迭代、公式法、矩阵方法等多种方法
下面给出了多种实现fibonacci（n）的方法，全部是用Python语句实现，
测试环境：Python3.8.6 64-bit Windows
Author: Liu Xiang
Email : liuxiangxyd@163.com
"""

import numpy as np  # 矩阵运算需要其中的Matrix类


class Fibase(object):
    """Fibonacci 基类，定义头两个数"""
    def __init__(self):
        self.a = 0
        self.b = 1
        self.name = 'Fibonacci'

class Fibonacci(Fibase):
    '''定义斐波那契数列类 Fibonacci(n,a=0,b=1), 生成器类'''

    def __init__(self, n, index=True) -> None:
        '''
        :param index: bool, 标识为 序列还是最大值？
        :param n: int, 当index=True时，生成第 n 个 Fibonacci数；
                  否则，生产不超过 n 的最大 Fibonacci数。
        '''
        super(Fibonacci, self).__init__()
        assert n>=0, '只能输入自然数'
        self.n = n
        self.curpos = 0
        self.index = index

    def __iter__(self):
        '''返回自己就行'''
        return self

    def __next__(self):
        ''' 迭代器中得到下一个 Fibonacci 数 '''
        first = self.a  # 保留第 0 个Fibonacci数: 0
        cond = self.curpos if self.index else first
        if cond <= self.n:
            self.a, self.b = self.b, self.a + self.b
            self.curpos += 1
            return first
        else:
            raise StopIteration

    def __str__(self):
        '''实例转换为字符串'''
        return '第 {0} 个 {1} 是 {2}'.format(self.curpos, self.name, self.a)

    def __repr__(self):  # TODO
        return f'Fibonacci({self.number})'

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
    #类方法推荐使用类名直接调用，当然也可以使用实例对象来调用（不推荐）
    #@classmethod


    #静态方法，不强制要求传递参数
    #静态方法的调用，既可以使用类名，也可以使用类对象，
    #@staticmethod
    #在实际编程中，几乎不会用到类方法和静态方法，因为我们完全可以使用函数代替
    # 它们实现想要的功能，但在一些特殊的场景中（例如工厂模式中），
    # 使用类方法和静态方法也是很不错的选择。
 

def fibo_number(n, a=0, b=1):
    """推荐该算法: 不含递归的最佳算法。
    # fibo_number(n): 非常简单的while循环方法，充分利用Python的三元操作符。
    # simple swap method: a, b, n = b, a+b, n-1
    # 测试 1000 以上没有问题。其它递归肯定慢，且会超过递归深度。
    """
    assert n >= 0, 'n为自然数'
    a, b = a, b
    if n==0:
        return n
    while (n):
        a, b, n = b, a+b, n-1
    return a


def fibo_yield(n, a=0, b=1):
    """强烈推荐该算法: 不含递归的最佳生成器算法。
    利用yield生成器方法: 生成 0...n 个Fibonacci数(共 n+1 个，含第0个)
    :param n: 序列最大值
    :param a, b: 第 0,1 个 Fibonacci数, 缺省为 0,1
    """
    assert n >= 0, 'n为自然数'
    a, b = a, b
    while n >= 0:
        yield a
        n, a, b = n-1, b, a+b


def fibo_index(n):
    """用黄金分割数来计算第n个斐波那契数"""
    from sympy import sqrt, Pow

    assert n >= 0, 'n为自然数'
    phi = (sqrt(5)+1)/2   #\frac{\sqrt{5}+1}{2}
    return ((Pow(phi, n) - Pow((-1/phi),n))/sqrt(5)).simplify()  #int()
     


def fibo_iteral(n, a=0, b=1):
    """不推荐该递归算法，n=1000时，RecursionError: maximum recursion depth exceeded
    # fibo_iteral(n): 递归迭代函数。
    # using iterating method
    """
    assert n >= 0, 'n为自然数'
    def fib_iter(n, x, y):
        if n == 0:
            return x
        else:
            return fib_iter(n-1, y, x+y)

    return fib_iter(n, a, b)


def fibo_lambda(n, a=0, b=1):
    """不推荐该递归算法，n=1000时，RecursionError: maximum recursion depth exceeded
    # fibo_lambda(n): 最精简的一条语句定义递归函数，三元操作符和递归结合。
    # using lambda and bool variable
    # 等价于一条语句 fib = lambda n, x=0, y=1: x if not n else fib(n-1,y,x+y)
    """
    assert n >= 0, 'n为自然数'
    __f = lambda n, x=a, y=b: x if not n else __f(n-1, y, x+y)
    return (__f(n))



def fibo_logical(n):
    """不推荐该递归算法。
    # fibo_logical(n): 递归迭代配合bool操作。
    # True = 1, False = 0, verify int(True) == 1, int(False) == 0
    """
    if n == 0:
        return 0
    else:
        return int(1 and n < 2) or fibo_logical(n-1) + fibo_logical(n-2)


def fibo_matrix_bakcup(n):
    """矩阵方法: [f_n f_{n-1}] = [f_{n-1} f_{n-2}]*M =...
    = [f_1,f_0]*M^{n-1} , M=matrix[[1,1],[1,0]]
    Using numpy.dot(A,B)，也可以用 pow(M,n)=M^n
    TODO: 如何改成符号运算，使之针对大数n不会溢出？
    """

    def mat_pow(n):
        '''numpy 中实现矩阵乘法是 O(log n)'''
        T = np.matrix("1 1;1 0", dtype='int64')
        return np.linalg.matrix_power(T, n)
        #pow(T, n) 当 n > 46 时，溢出

    assert n >= 0, 'n为自然数'
    if (n==0 or n==1):
        return n
    # fib list codes: 返回所有Fib数列
    res = []
    for i in range(n-1):
        res.append(np.array(mat_pow(i))[0][0])
    return res
    #return np.array(mat_pow(n-1))[0][0]
    

def fibo_matrix(n):
    '''矩阵方法: 
    [f_n f_{n-1}].T = M*[f_{n-1} f_{n-2}].T =...
    = M^{n-1}*[f_1,f_0].T, M = matrix[[1,1],[1,0]]
    f_n = M^{n-1}[0,0]
    '''
    from sympy import Pow, Matrix

    assert n >= 0, 'n为自然数'
    if (n==0 or n==1): return n
    return Pow(Matrix(2,2,[1,1,1,0]), n-1)[0,0]


def fibo_between(min=0, max=np.inf, step=1):
    """闭区间[min,max]内的Fibonacci数，间隔为 step"""
    if min < 0:
        min = 0
        
    left, right, step = min, max, step
    _fib = []
    _fibseries = Fibonacci(max)
    for _ in range(left):
        next(_fibseries)
    for i in range(left, right+1, step):
        _fib.append(next(_fibseries))
        for _ in range(step-1):  # skip step
            next(_fibseries)

    return _fib


def fibo_perfect(max):
    """Fibonacci Numbers with index == digit sum
    找出斐波那契数，满足数位之和==序数，如
    [0, 1, 5, 10, 31, 35, 62, 72, 175, 180, 216, 251, 252, 360, 494, 504, 540, 946, 1188, 2222](http://oeis.org/A020995)
    [0, 0], [1, 1], [5, 5], [10, 55], [31, 1346269], [35, 9227465], [62, 4052739537881], [72, 498454011879264]    
    """
    res = []
    
    for n in range(max):
        fib = fibo_number(n)
        if n == sum([int(s) for s in str(fib)]): 
            res.append([n, fib])

    return res


def quick_pow(x, n):
    """快速幂算法"""
    if n == 0: return 1
    t = 1
    while (n != 0):
        if (n & 1): t *= x  #奇数乘以x
        n >>= 1
        x *= x
  
    return t


def digitsum(n):
    #求数位之和, 可以写成一条语句
    s = str(n)
    sa = 0
    for a in s:
        sa += int(a)
    return sa


if __name__ == '__main__':
    # 测试多种方法得到的 Fibonacci数，给定序列数n，得到第n个Fibonacci数。测试通过OK
    
    num = 1000
    # fibList = quick_pow(2, num)
    # print(fibList)

    # for i in range(num-10, num):
    #     print(i, fibo_index(num),  fibo_number(num)) 
    
    
    # fib = Fibonacci(num, False)
    # print(list(fib))
    #fib = fibo_matrix(num)
    fib = fibo_SPow(num)
    print(num, fib, fibo_number(num))

    '''
    fib = Fibonacci()
    fib = fibo.fwhile(4)
    for f in fib:
        print(f)

    for i in range(15,30):
        print("{i}：Recursive={R} While={W} Logical={L} Iteral={T} Lambda={A}".format(i=i+1,
            R=fibo_recursive(i), W=fibo_number(i), L=fibo_logical(i), T=fibo_iteral(i), A=fibo_lambda(i)))
    
    for i in range(15):
        print("Index=", i, "Recursive=", fibo_recursive(i),
              "While=", fibo_number(i), "Logical=", fibo_logical(i),
              "Iteral=", fibo_iteral(i), "Lambda=", fibo_lambda(i))
    '''