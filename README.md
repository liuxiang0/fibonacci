# 斐波那契数列 Fibonacci Numbers

本文介绍了多种方式得到斐波那契数列或斐波那契数。斐波那契数列也称为“兔子数列”。来源于兔子生产的预测。

**Fibonacci 数列**定义为：
\(F_0=0, F_1=1, F_{n}=F_{n-1}+F_{n-2}; n\geq 2, n\in \mathbb{N}^+\)  

下面这段代码就是Python 的SymPy库中提供的Fibonacci类 `fibonacci(n, Sym=None)`   

~~~python
>>> from sympy import fibonacci
>>> prev10 = [fibonacci(n) for n in range(10)]
>>> prev10
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
~~~

很显然，斐波那契数列都是自然数，但是却可以用公式表示每一项：  
\(F_n = \dfrac{1}{\sqrt5}\left((\dfrac{1+\sqrt5}{2})^n - (\dfrac{1-\sqrt5}{2})^n\right),\) 简写为   
\(F_n=\frac{1}{\sqrt5}(\phi^n-(-\phi^{-1})^n)\)

\(F_z = \frac{\phi^z - \cos(\pi z) \phi^{-z}}{\sqrt 5}; z\in \mathbb{N}, z\) 还可以扩充为实数和复数。   
此处 \(\phi =\frac{1+\sqrt{5}}{2}\) 为黄金分割比（`S.GoldenRatio`）

~~~python
>>> from sympy import sqrt, cos
>>> from sympy.abc import x,y,z
>>> phi = (sqrt(5)+1)/2
>>> p = (phi**z-cos(pi*z)*phi**(-z))/sqrt(5)
>>> fib = [p.subs({z:n}).simplify() for n in range(11)]
>>> fib
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
~~~

用Python实现，采用递归、迭代、三元操作符、逻辑运算多种方法，得到斐波那契数列

## 斐波那契多项式 Fibonacci Polynomials

定义：\(F_1(z) = 1, F_2(z) = z,\)    
\(F_n(z) = z*F_{n-1}(z) + F_{n-2}(z);\)   
\(\forall n > 2, n \in \mathbb{N}^+, F_n(1) = F_n, z\in \mathbb{C}\).

 
## Fibonacci Day (斐波那契日11月23日)

11月23日（11/23)就是著名的**斐波那契日**, 代表了 斐波那契数列前4项 \{1,1,2,3\}。

这个独特的数字序列是1202年由意大利数学家比萨的莱昂纳多（死后被称为斐波纳契）在其革命性的作品《Liber Abaci》中介绍到了欧洲。这本书开篇就描述了印度-阿拉伯数字系统或 "印度模式"-`0 1 2 3 4 5 6 7 8 9`，说明它们的应用可以简化贸易，使计算更快、更容易（这时欧洲大部分地区使用罗马数字）。

在该书的第三部分，斐波那契继续描述各种数学问题，包括一个关于兔子数量增加的实验，结果就是斐波那契数列。这个序列是通过将前两个数字相加来确定下一个数字：1、1、2、3、5、8、13、21、34，等等。从那时起，数学家、科学家和艺术家一直在研究和应用斐波那契数列和构成它的斐波那契数字。虽然斐波纳契得到了这项工作的荣誉，但他并不是第一个发现这项工作的人。1985年发表的研究报告认为，在斐波纳契工作之前的一个多世纪，古印度数学家就已经意识到并写下了这个序列。

## **递归方法：fibo_recursive**
 
    # fibo_recursive(n): 要求很简单，输入n，输出第n个Fibonacci数，n为正整数。
    # algorithm: 递归算法recursive，耗资源比较大


## **三元操作符：fibo_number(n,a=0,b=1)**

推荐该算法: 不含递归的最佳算法。  
fibo_number(n): 非常简单的while循环方法，充分利用Python的三元操作符: a, b, n = b, a+b, n-1  
测试 1000 以上没有问题。其它递归肯定慢，且会超过递归深度。

## **三元操作生成器方法：fibo_yield(n, a=0, b=1)**

强烈推荐该算法: 不含递归的最佳生成器算法。  
利用 `yield` 生成器方法: 生成 0...n 个Fibonacci数(共 n+1 个，含第0个)   
:param n: 序列最大值   
:param a, b: 第 0, 1个 Fibonacci数, 缺省为 0,1

## **公式法直接得到：fibo_index(n)**

用黄金分割数来计算第 n 个斐波那契数   
\(F_n = \dfrac{\phi^n - (-\phi^{-1})^n}{\sqrt5}\)

## **递归迭代算法：fibo_iteral(n, a=0, b=1)**

不推荐该递归算法，n=1000 时，报错误信息：   
RecursionError: maximum recursion depth exceeded  
定义递归‘迭代’函数。

## **匿名函数结合三元操作符：fibo_lambda(n, a=0, b=1)**

最精简的一条语句定义递归函数，三元操作符和递归结合。  
不推荐该递归算法, 本质上还是递归定义。  
等价于一条语句 fib = lambda n, x=0, y=1: x if not n else fib(n-1,y,x+y)

## **递归结合逻辑运算：fibo_logical(n)**

不推荐该递归算法，递归迭代配合bool操作。  
True = 1, False = 0, verify int(True) == 1, int(False) == 0

## **矩阵方法**

不推荐该算法, 局限: 当 n > 46，即出现溢出，得到负数.   

定义矩阵 \(M = \begin{pmatrix} 1 & 1\\1 & 0 \end{pmatrix}\)

\(\begin{pmatrix} F_n \\ F_{n-1}\end{pmatrix}= M^{n-1} \begin{pmatrix} F_1 \\ F_0\end{pmatrix}\)

初始值 \(F_1=1,F_0 =0\)

该方法还可以用到幂函数的快速算法求 \(M^n\)


## **获得指定区间上的Fibonacci数列：fibo_between(min=0, max=np.inf, step=1)**

闭区间 `[min,max]` 内的 Fibonacci 数列，可以设置间隔，缺省 step=1