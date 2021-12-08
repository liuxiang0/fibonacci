# 斐波那契数列 Fibonacci Numbers

**Fibonacci 数列**定义为：
$F_0=0, F_1=1, F_{n}=F_{n-1}+F_{n-2}; n\geq 2, n\in \mathbb{N}^+$  

~~~python
>>> from sympy import fibonacci
>>> prev10 = [fibonacci(n) for n in range(10)]
>>> prev10
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
~~~

很显然，斐波那契数列都是自然数，但是却可以用公式表示每一项：  
$F_n = \dfrac{1}{\sqrt5}\left((\dfrac{1+\sqrt5}{2})^n - (\dfrac{1-\sqrt5}{2})^n\right)$

$F_z = \frac{\phi^z - \cos(\pi z) \phi^{-z}}{\sqrt 5}; z\in \mathbb{N}, z$ 还可以扩充为实数和复数。此处 $\phi =\frac{1+\sqrt{5}}{2}$ 为黄金分割比（`S.GoldenRatio`）

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

定义：$F_1(z) = 1, F_2(z) = z, F_n(z) = z*F_{n-1}(z) + F_{n-2}(z); \forall n > 2, n \in \mathbb{N}^+, F_n(1) = F_n, z\in \mathbb{C}$.


## Fibonacci Day (斐波那契日11月23日)

11月23日（11/23)就是著名的**斐波那契日**, 代表了 斐波那契数列前4项 \{1,1,2,3\}。

这个独特的数字序列是1202年由意大利数学家比萨的莱昂纳多（死后被称为斐波纳契）在其革命性的作品《Liber Abaci》中介绍到了欧洲。这本书开篇就描述了印度-阿拉伯数字系统或 "印度模式"-`0 1 2 3 4 5 6 7 8 9`，说明它们的应用可以简化贸易，使计算更快、更容易（这时欧洲大部分地区使用罗马数字）。

在该书的第三部分，斐波那契继续描述各种数学问题，包括一个关于兔子数量增加的实验，结果就是斐波那契数列。这个序列是通过将前两个数字相加来确定下一个数字：1、1、2、3、5、8、13、21、34，等等。从那时起，数学家、科学家和艺术家一直在研究和应用斐波那契数列和构成它的斐波那契数字。虽然斐波纳契得到了这项工作的荣誉，但他并不是第一个发现这项工作的人。1985年发表的研究报告认为，在斐波纳契工作之前的一个多世纪，古印度数学家就已经意识到并写下了这个序列。

## **递归方法：fibo_recursive**
 
    # fibo_recursive(n): 要求很简单，输入n，输出第n个Fibonacci数，n为正整数。
    # algorithm: 递归算法recursive，耗资源比较大


## **三元操作符：fibo_while**

    # fibo_while(n): 非常简单的while循环方法，充分利用Python的三元操作符。
    # simple swap method: a, b, n = b, a+b, n-1

## **递归结合逻辑运算：fibo_logical**

    # fibo_logical(n): 递归迭代配合bool操作。
    # True = 1, False = 0, verify int(True) == 1, int(False) == 0

## **迭代算法：fibo_iteral**

    # fibo_iteral(n): 定义递归‘迭代’函数。
    # using iterating method

## **匿名函数结合三元操作符：fibo_lambda**

    # fibo_lambda(n): 最精简的一条语句定义递归函数，三元操作符和递归结合。
    # using lambda and bool variable

## **矩阵方法**

定义矩阵 $M = \begin{pmatrix} 1 & 1\\1 & 0 \end{pmatrix}$

\(\begin{pmatrix} F_n \\ F_{n-1}\end{pmatrix}= M^{n-1} \begin{pmatrix} F_1 \\ F_0\end{pmatrix}\)
