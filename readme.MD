# Fibonacci Number（斐波那契数列）

  用Python实现，采用递归、迭代、三元操作符、逻辑运算多种方法，得到斐波那契数列

## Fibonacci Day
1, 1, 2, 3: It's Fibonacci Day!
Today's date, November 23, can be represented as 11/23, or 1,1,2,3—a Fibonacci sequence of numbers. Likewise, as the leaves on the Queen Victoria agave in today's image spiral out from the center, they also express the Fibonacci sequence. This unique sequence of numbers was introduced to Europe in 1202 by the Italian mathematician Leonardo of Pisa (posthumously named Fibonacci) in his revolutionary work the 'Liber Abaci.' The book begins by describing the Hindu-Arabic numeral system or 'Modus Indorum’—0 1 2 3 4 5 6 7 8 9—showing how their application could simplify trade and make calculations faster and easier (most of Europe at this time used Roman numerals).

In the third section of his book, Fibonacci goes on to describe various mathematical problems including a thought experiment about increasing rabbit populations, which results in a Fibonacci sequence. The sequence is determined by adding the previous two numbers together to determine the next number: 1, 1, 2, 3, 5, 8, 13, 21, 34, etc. Since then, mathematicians, scientists, and artists have been studying and applying the Fibonacci sequence and the Fibonacci numbers that make it up. While Fibonacci gets the credit for this work, he wasn't the first to discover it. Research published in 1985 posits that ancient Indian mathematicians had been aware of and written about the sequence for more than a century before Fibonacci's work.

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

