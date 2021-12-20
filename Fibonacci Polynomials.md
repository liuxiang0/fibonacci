# 斐波那契多项式(Fibonacci Polynomials)

上一篇讲了 斐波那契数列，本篇讲 斐波那契函数。

## 函数定义始于多项式递归定义

定义(Definition):  
$(1)\; f_0(z) = 1, f_1(z) = z,$  
$(2)\; f_n(z) = z*f_{n-1}(z) + f_{n-2}(z);$  
$\forall n > 1, n \in \mathbb{N}^+, f_n(1) = F_n, z\in \mathbb{C}$.

写全了就是如下的序列：

$f_0(z) = 1$  
$f_1(z) = z$  
$f_2(z) = z^{2} + 1$  
$f_3(z) = z^{3} + 2 z$  
$f_4(z) = z^{4} + 3 z^{2} + 1$  
$f_5(z) = z^{5} + 4 z^{3} + 3 z$  
$f_6(z) = z^{6} + 5 z^{4} + 6 z^{2} + 1$  
$f_7(z) = z^{7} + 6 z^{5} + 10 z^{3} + 4 z$  
$f_8(z) = z^{8} + 7 z^{6} + 15 z^{4} + 10 z^{2} + 1$  
$f_9(z) = z^{9} + 8 z^{7} + 21 z^{5} + 20 z^{3} + 5 z$  
......

~~~python
>>> from sympy import fibonacci, latex
>>> from sympy.abc import z

>>> fibz=[fibonacci(n,z) for n in range(1,11)]
>>> fibz
[1, z, z**2 + 1, z**3 + 2*z, z**4 + 3*z**2 + 1, z**5 + 4*z**3 + 3*z, z**6 + 5*z**4 + 6*z**2 + 1, z**7 + 6*z**5 + 10*z**3 + 4*z, z**8 + 7*z**6 + 15*z**4 + 10*z**2 + 1, z**9 + 8*z**7 + 21*z**5 + 20*z**3 + 5*z]
>>> for n, f in enumerate(fibz): print("$f_{0}(z) = {1}$   ".format(n, latex(f)))
~~~
