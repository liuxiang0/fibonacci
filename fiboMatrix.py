"""采用矩阵运算方法计算Fibonacci数
    1. 用numpy的矩阵运算，存在64位限制，n=93 会溢出。
    2. 用sympy的矩阵符号运算，不存在溢出问题。
"""

# 1. 使用 numpy 的矩阵运算得到 斐波那契数列
import numpy as np
def fibo_Matrix_tool(n):
    # 初始化矩阵 M = [1,1,],[1,0]]
    Matrix = np.matrix("1 1;1 0", dtype='int64')
    # 返回是matrix类型 M**n, M^n
    return np.linalg.matrix_power(Matrix, n)

def fibo_Matrix_np(n):
    '''通过矩阵的幂运算，得到新矩阵，因为初始值为[1,0],所以新矩阵的[0,0]就是所求'''

    assert n>=0, '请指定自然数'
    result_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55] #0-10不用计算了
    if n < 11: return result_list[:n+1]
    for i in range(10, n):
        result_list.append(np.array(fibo_Matrix_tool(i))[0][0])
    return result_list

# 2、上述算法缺陷是当n比较大时，会溢出。下面改为符号运算，可以进行大数据的计算而不会溢出。

def fibo_matrix(n):
    '''矩阵方法: 
    [f_n f_{n-1}].T = M*[f_{n-1} f_{n-2}].T =...
    = M^{n-1}*[f_1,f_0].T, M = matrix[[1,1],[1,0]]
    f_n = M^{n-1}[0,0], 因为 [f_1,f_0]=[1,0], 乘法的结果就是矩阵第一个数。
    '''
    from sympy import Pow, Matrix

    assert n >= 0, 'n必须为自然数'
    if (n==0 or n==1): return n
    return Pow(Matrix(2,2,[1,1,1,0]), n-1)[0,0]


# 调用
if __name__ == '__main__':
    num = 93
    print("{0} FiboNum={1} by Numpy".format(num, fibo_Matrix_np(num)))
    num = 100000
    print("{0}th FiboNum={1} by Sympy".format(num, fibo_matrix(num)))
