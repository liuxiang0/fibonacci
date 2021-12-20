# 斐波那契数列 Fibonacci Sequence

本文介绍了多种方式得到斐波那契数列或斐波那契数。斐波那契数列也称为“兔子数列”。来源于兔子繁殖的预测。它的重要性体现在相邻两数之比趋向黄金分割数，自然界很多现象也可找到它的身影，画图还与漂亮的螺旋线有关。

介绍自然界中的 Fibonacci 数，参见网站 [自然界中的斐波那契数](https://insteading.com/blog/fibonacci-sequence-in-nature/ "The Fibonacci Sequence in Nature")

**Fibonacci 数列**定义为：  
$F_0=0, F_1=1, F_{n}=F_{n-1}+F_{n-2}; n\geq 2, n\in \mathbb{N}^+$  
也可以写成函数形式，关于整数的函数:  
$f(n)=\begin{cases} \qquad\qquad 0 &, n=0\\ \qquad\qquad 1 &, n=1\\ f(n-1)+f(n-2) &,n>=2\end{cases}$

也属于一种特殊的整数数列，详细参考**在线整数数列百科** [1][1_OEIS]

下面这段代码就是 Python 的 SymPy 库中提供的 Fibonacci类 `fibonacci(n, Sym=None)`  

~~~python
>>> from sympy import fibonacci
>>> prev10 = [fibonacci(n) for n in range(10)]
>>> prev10
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
~~~

## 斐波那契数及其数列的属性

### 1. 通项公式是奇妙的无理数公式组合

很显然，斐波那契数列都是**自然数**，但是却可以用**含有无理数**的公式表示每一项：  
$F_n = \frac{1}{\sqrt5}\left((\frac{1+\sqrt5}{2})^n - (\frac{1-\sqrt5}{2})^n\right),$ 也称为 **Binet公式** [2][2_Binet]  
简写为  $F_n=\frac{1}{\sqrt5}(\phi^n-(-\phi^{-1})^n)$

$F_z = \frac{\phi^z - \cos(\pi z) \phi^{-z}}{\sqrt 5}; z\in \mathbb{N}, z$ 还可以扩充为实数和复数。  
此处 $\phi =\frac{1+\sqrt{5}}{2}$ 为黄金分割比率（`S.GoldenRatio`）

求解过程可以用特征值法，求出 $x^2=x+1$ 的两个特征值 $\lambda_{1,2}=\frac{1\pm\sqrt{5}}{2},$ 通项为 $f(n)=c_1\lambda_1^n+c_2\lambda_2^n,$ 再由初始条件：$f(0)=0, f(1)=1,$ 得到方程组：  
$\begin{cases}
    c_1+c_2=0 \\
    c_1\lambda_1+c_2\lambda_2=1
\end{cases}$

解得： $c_1 = -c_2 = \dfrac{1}{\lambda_1-\lambda_2}=\dfrac{1}{\sqrt{5}}, f(n)=\dfrac{\lambda_1^n-\lambda_2^n}{\lambda_1-\lambda_2}.$

~~~python
>>> from sympy import sqrt, cos
>>> from sympy.abc import x,y,z
>>> phi = (sqrt(5)+1)/2
>>> p = (phi**z-cos(pi*z)*phi**(-z))/sqrt(5)
>>> fib = [p.subs({z:n}).simplify() for n in range(11)]
>>> fib
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
~~~

#### 1.1 Binet公式的推论: $f(n+1) = \text{round}(f(n)\times\phi)$

通过Binet公式不难发现，[Fibonacci数只与前面的项有关系][fibsection4]，这是因为  
$\phi=\frac{1+\sqrt{5}}{2}\approx 1.618, 1-\phi=\frac{1-\sqrt{5}}{2}\approx -0.618, f(n)=\frac{\phi^n}{\sqrt{5}} - \frac{(1-\phi)^n}{\sqrt{5}} = \text{round}(\frac{\phi^n}{\sqrt{5}})$

通过前一个数乘以黄金比率，再四舍五入法取整(`round(x)`)，就得到了下一个Fibonacci数。

$f(n+1) = \text{round}(f(n)\times\phi); \; \forall n\ge 2,  n\in \mathbb{N}^+$. 尾数忽略不计，位数变化情况如下：

~~~python
>>> from sympy import S, sqrt
>>> [((1-S.GoldenRatio)**n/sqrt(5)).evalf(10) for n in range(2,10)]
[0.1708203933, -0.1055728090, 0.06524758425, -0.04032522475, 0.02492235950, -0.01540286525, 0.009519494249, -0.005883371002]
~~~

#### 1.2 Fibonacci数的位数判断: $\text{round}(n\times \log(\phi) - \frac{1}{2}\log{5})$

因为 $f(n)=\frac{\phi^n}{\sqrt{5}} - \frac{(1-\phi)^n}{\sqrt{5}},$ 所以取对数，得到：

$\log{f(n)} = n\times \log(\phi) - \log\sqrt{5}= n\times \log(\phi) - \frac{1}{2}\log{5},$ 后面一项不影响位数的变化，可以忽略不计。

从而 $f(n)$ 的位数为 $1 + \text{int}(n\times \log(\phi) - \frac{1}{2}\log{5}); \text{int}(x)=\text{floor}(x)\le x,$ 表示不超过 $x$ 的整数。

~~~python
>>> from sympy import fibonacci as fib
>>> from sympy import S, log
>>> [1+int(n*log(S.GoldenRatio,10)-log(5,10)/2) for n in range(2,50)]
[1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10]
>>> [len(str(fib(n))) for n in range(2,50)]
[1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 9, 10, 10, 10, 10, 10]
>>> [len(str(fib(n))) for n in range(2,50)]== [1+int(n*log(S.GoldenRatio,10)-log(5,10)/2) for n in range(2,50)]
True
~~~

#### 1.3 已知Fibonacci数 $f(n)$，求 $n$

因为 $f(n)\approx \phi^n/\sqrt{5}\implies n\approx\ln[\sqrt{5}f(n)]/\ln\phi=[\frac{1}{2}\ln5+\ln{f(n)}]/\ln\phi$

如果给定的数不是Fibonacci数，则上述计算公式得到的可能是分数，但是也是接近某个Fibonacci数的分数。由此公式还可以得到不大于N，最接近N 的Fibonacci数 $f(n)$。  

$n = \text{int}([\frac{1}{2}\ln5+\ln{N}]/\ln\phi)$

~~~python
>>> [int((log(5)/2+log(n))/log(S.GoldenRatio)) for n in [1000,2000,3000,4000,70000,90000]]
[16, 17, 18, 18, 24, 25]
>>> [fibonacci(n) for n in [16, 17, 18, 18, 24, 25]]
[987, 1597, 2584, 2584, 46368, 75025]
~~~

### 2. 与数列求和相关的性质 [3][3_FibProperty]

- 快速求前n项之和 $F_1+F_2+...+F_n=F_{n+2}-1$
- 奇数项之和 $F_1+F_3+...+F_{2n-1}=F_{2n}$
- 偶数项之和 $F_2+F_4+...+F_{2n} = F_{2n+1}-1$
- 交替之和 $F_1-F_2+F_3-F_4+...+(-1)^{n+1}F_{n} = (-1)^{n+1}F_{n-1}+1$
- 平方和 $F_1^2+F_2^2+...+F_n^2 = F_n\cdot F_{n+1}$
- 下标和 $F_{n+m} = F_{n-1}\cdot F_{m} + F_{n} \cdot F_{m+1}$
- 平方差公式 $F_{n+1}^2-F_{n-1}^2 = F_{2n}^2$
- 最大公约数 $\gcd(f(n), f(m)) = f({\gcd(n, m)}),$  反证法可证相邻两个斐波那契数必定互素，辗转相减法可证其它。
- 等价式 $n\mid m \iff F_n \mid F_m$
- 连续三个数关系（三胞胎） $F_{n+1}\cdot F_{n-1} - F_n^2 = (-1)^n$

### 3. 相邻两项的比值‘逼近’黄金分割率(Golden Ratio)

$\displaystyle\lim_{n \to \infty}\dfrac{F_n}{F_{n-1}} = \phi = \dfrac{1+\sqrt{5}}{2}\approx 1.618$

收敛速度很快，从下面看出，第20项就达到了小数点后9位精度。

~~~python
>>> ((1+sqrt(5))/2).evalf(10)
1.618033989
>>> [(fibonacci(n)/fibonacci(n-1)).evalf(9) for n in range(10,30)]
[1.61764706, 1.61818182, 1.61797753, 1.61805556, 1.61802575, 1.61803714, 1.61803279, 1.61803445, 1.61803381, 1.61803406, 1.61803396, 1.61803400, 1.61803398, 1.61803399, 1.61803399, 1.61803399, 1.61803399, 1.61803399, 1.61803399, 1.61803399]
~~~

### 4. Fibonacci数的模态(modulo)具有周期性

$F\mod 2=[1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1],$  
$F\mod 3=[1, 1, 2, 0, 2, 2, 1, 0, 1, 1, 2, 0, 2, 2, 1, 0, 1, 1, 2, 0, 2, 2, 1, 0, 1, 1, 2, 0, 2],$  
$F\mod 4=[1, 1, 2, 3, 1, 0, 1, 1, 2, 3, 1, 0, 1, 1, 2, 3, 1, 0, 1, 1, 2, 3, 1, 0, 1, 1, 2, 3, 1],$  
$F\mod 5=[1, 1, 2, 3, 0, 3, 3, 1, 4, 0, 4, 4, 3, 2, 0, 2, 2, 4, 1, 0, 1, 1, 2, 3, 0, 3, 3, 1, 4],$  
$F\mod 6=[1, 1, 2, 3, 5, 2, 1, 3, 4, 1, 5, 0, 5, 5, 4, 3, 1, 4, 5, 3, 2, 5, 1, 0, 1, 1, 2, 3, 5],$  
$F\mod 7=[1, 1, 2, 3, 5, 1, 6, 0, 6, 6, 5, 4, 2, 6, 1, 0, 1, 1, 2, 3, 5, 1, 6, 0, 6, 6, 5, 4, 2],$  
$F\mod 8=[1, 1, 2, 3, 5, 0, 5, 5, 2, 7, 1, 0, 1, 1, 2, 3, 5, 0, 5, 5, 2, 7, 1, 0, 1, 1, 2, 3, 5],$  
$F\mod 9=[1, 1, 2, 3, 5, 8, 4, 3, 7, 1, 8, 0, 8, 8, 7, 6, 4, 1, 5, 6, 2, 8, 1, 0, 1, 1, 2, 3, 5],$  

设周期函数为 $p(k)$, 则有  
$\{p(k), k=2,3,...,20\} = \{3,8,6,20,24,16,12,24,60,10,24,28,48,40,24,36,24,18,60\}$

~~~python
>>> [[fibonacci(n)% k for n in range(1, 30)] for k in range(2, 10)]
~~~

### 5. 斐波那契多项式(Fibonacci Polynomials)

定义(Definition)：  
$F_1(z) = 1, F_2(z) = z,$  
$F_n(z) = z*F_{n-1}(z) + F_{n-2}(z);$  
$\forall n > 2, n \in \mathbb{N}^+, F_n(1) = F_n, z\in \mathbb{C}$.

### 6. 神秘的斐波那契数 89 的倒数(reciprocal)

神奇的分数 $\frac{1}{89} = 0.\dot{0}112359550561797752808988764044943820224719\dot{1}$  

将每个斐波那契数通过变换 $F_n\times 10^{-n-1}$ 变成小数数列，再求和, 即得到分数 $\frac{1}{89},$ 这不是巧合， 可以证明 [4][4_89的倒数]。

~~~python
>>>> sum([fibonacci(k)*Rational(1,10**(k+1)) for k in range(100)]).evalf(50)
0.011235955056179775280898876404494382022471910112360
>>> Rational(1,89).evalf(50)
0.011235955056179775280898876404494382022471910112360
~~~

### 7. 负下标表示的斐波那契数

如果允许下标为负数，则有 $F_{-n} = (-1)^{n+1} F_n$  

~~~python
>>> [fibonacci(n) for n in range(-10,11)]
[-55, 34, -21, 13, -8, 5, -3, 2, -1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
~~~

### 8. 斐波那契日(Fibonacci Day: 11月23日)

11月23日（11/23)就是著名的**斐波那契日**, 代表了 斐波那契数列前4项 \{1,1,2,3\}。

这个独特的数字序列是1202年由意大利数学家**莱昂纳多.比萨(Leonardo di Pisa)**在其革命性的作品《**Liber Abaci**》中介绍到了欧洲。外号 Fibonacci（斐波那契，意即 Son of Bonacci）, 这本书开篇就描述了印度-阿拉伯数字系统或 "印度模式"-`0 1 2 3 4 5 6 7 8 9`，说明它们的应用可以简化贸易，使计算更快、更容易（这时欧洲大部分地区使用罗马数字）。

在该书的第三部分，斐波那契继续描述各种数学问题，包括一个关于兔子数量增加的实验，结果就是斐波那契数列。假设一对兔子（雌雄各一个）每月产一对小兔崽子（也是雌雄各一个），而每对小兔子，需要生长一个月后才能称为能繁殖的大兔子。则可以总结规律如下：  
（1）每个月小兔子对数 = 上个月大兔子对数；  
（2）每个月大兔子对数 = 上个月大兔子对数 + 上个月小兔子对数；  
（3）每个月大兔子对数 = 上个月大兔子对数 + 上上个月大兔子对数；  
（4）兔子不会死掉。

这个序列是通过将前两个数字相加来确定下一个数字：`1、1、2、3、5、8、13、21、34、55、89...`。从那时起，数学家、科学家和艺术家一直在研究和应用斐波那契数列和构成它的斐波那契数字。

## Python编程实现

用Python实现，采用递归、迭代、三元操作符、逻辑运算多种方法，得到斐波那契数列

### 1. **三元操作符：fibo_number(n, a=0, b=1)**

推荐该算法: 不含递归的最佳算法。  
`fibo_number(n,a=0,b=1)`: 非常简单的 `while` 循环方法，
充分利用Python的三元操作符: `a, b, n = b, a+b, n-1`  
测试 1000 以上没有问题。其它递归肯定慢，且会超过递归深度。

### 2. **三元操作生成器方法：fibo_yield(n, a=0, b=1)**

强烈推荐该算法: 不含递归的最佳生成器算法。  
利用 `yield` 生成器方法: 生成 `0...n` 个Fibonacci数(共 n+1 个，含第0个)  
`:param n:` 序列最大值  
`:param a, b:` 第 `0, 1` 个 Fibonacci 数, 缺省为 `0,1`

### 3. **公式法直接得到：fibo_index(n)**

用黄金分割数来计算第 n 个斐波那契数  
$F_n = \frac{\phi^n - (-\phi^{-1})^n}{\sqrt5} = \frac{\phi^n - (1-\phi)^n}{\sqrt5}$, 其中的幂指数用符号运算:  
`((sympy.Pow(phi, n) - sympy.Pow((-1/phi),n))/sqrt(5)).simplify()`

如果令 $\alpha = \frac{1+\sqrt{5}}{2}, \beta=\frac{1-\sqrt{5}}{2},$  
显然 $\alpha+\beta=1,  \alpha\cdot \beta=-1,$  
满足 $x^2-x-1=0,$
此时 $F_n = \dfrac{\alpha^n-\beta^n}{\sqrt{5}}$

### 4. **递归迭代算法：fibo_iteral(n, a=0, b=1)**

不推荐该递归算法，n=1000 时，报错误信息：超出了递归深度  
`RecursionError: maximum recursion depth exceeded`  
定义递归‘迭代’函数。

### 5. **匿名函数结合三元操作符：fibo_lambda(n, a=0, b=1)**

最精简的一条语句定义递归函数，三元操作符和递归结合。  
不推荐该递归算法, 本质上还是递归定义。  
等价于一条语句 `fib = lambda n, x=0, y=1: x if not n else fib(n-1,y,x+y)`

### 6. **递归结合逻辑运算：fibo_logical(n)**

不推荐该递归算法，递归迭代配合bool操作。  
`True = 1, False = 0, verify int(True) == 1, int(False) == 0`

### 7. **矩阵方法**

定义矩阵 $M = \begin{pmatrix} 1 & 1\\1 & 0 \end{pmatrix}$

$\begin{pmatrix} F_n \\ F_{n-1}\end{pmatrix}=M\begin{pmatrix} F_{n-1} \\ F_{n-2}\end{pmatrix}=\cdots= M^{n-1} \begin{pmatrix} F_1 \\ F_0\end{pmatrix}$

初始值 $F_1=1,F_0 =0$

该方法还可以用到矩阵的**快速幂算法** [5][5_QuicklyPow]，即二分递归：  
$M^n=\text{sympy.Pow}(M,n)=\begin{cases} M^{n>>1}\cdot M^{n>>1}, & n \mod 2=0 \\ M\cdot M^{(n+1)>>1}\cdot M^{(n+1)>>1}, & n \mod 2=1
\end{cases}$

$n>>1$ 表示右移一位，即 $n = \frac{n}{2}$

经过测试，用 SymPy 的符号运算（`Pow`），可以计算大数 $n$，不会产生溢出。一条语句就可以得到 `sympy.Pow(sympy.Matrix(2,2,[1,1,1,0], n-1))[0,0]`

用 Python 内置函数 `pow(a,n)`(n > 46时溢出，32位整数限制) 或 numpy 库中的 `numpy.linalg.matrix_power(T, n)` (n稍大也会出现溢出错误，64位整数限制)。

### 8. **获得指定区间上的Fibonacci数列：fibo_between(min=0, max=np.inf, step=1)**

闭区间 `[min,max]` 内的 Fibonacci 数列，可以设置间隔，缺省间隔 `step=1`

### 9. **Python类方法实现**

更多更新的代码参见 [我的github网站](https://github.com/liuxiang0/fibonacci)

## 参考资料

The Best Books about Fibonacci and the Fibonacci Sequence

1、[The Golden Ratio: The Story of PHI, the World’s Most Astonishing Number](https://www.amazon.com/dp/0767908163/?tag=nfthmstd-20) by Mario Livio

2、[Growing Patterns: Fibonacci Numbers in Nature](https://www.amazon.com/dp/1590787528/?tag=nfthmstd-20) by Sarah and Richard Campbell

3、[The Golden Section: Nature’s Greatest Secret](https://www.amazon.com/dp/0802715397/?tag=nfthmstd-20) by Scott Olsen

4、[The Fabulous Fibonacci Numbers](https://www.amazon.com/dp/1591024757/?tag=nfthmstd-20) by Alfred Posamentier and Ingmar Lehmann

5、[Blockhead: The Life of Fibonacci](https://www.amazon.com/dp/0805063056/?tag=nfthmstd-20) by Joseph D’Agnese and John O’Brien (children’s book, named a [Mathical Honor Book](https://mathicalbooks.org/2015/04/award-winners-announced/) April 2015)

[1_OEIS]: http://oeis.org/A000045 "在线整数数列公益网站"

[2_Binet]: http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html

[fibsection4]: http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html#section4

[3_FibProperty]: https://www.whitman.edu/Documents/Academics/Mathematics/clancy.pdf "Fibonacci Numbers by TYLER CLANCY"

[4_89的倒数]: http://www2.math.ou.edu/~dmccullough/teaching/miscellanea/miner.html "The Remarkable Number 1/89 by Robert Miner"
<!--[The Remarkable Number 1/89 by Robert Miner]-->

[5_QuicklyPow]: https://baike.baidu.com/item/%E5%BF%AB%E9%80%9F%E5%B9%82?fr=aladdin "快速密算法"
