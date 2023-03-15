from operator import add, sub


def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    >>> a_plus_abs_b(-1, 4)
    3
    >>> a_plus_abs_b(-1, -4)
    3
    """
    if b < 0:
        f = sub # 注意最后输出的f是一个函数，所以需将f设为add或sub函数
    else:
        f = add
    return f(a, b)


def a_plus_abs_b_syntax_check():
    """Check that you didn't change the return statement of a_plus_abs_b.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, re
    >>> re.findall(r'^\s*(return .*)', inspect.getsource(a_plus_abs_b), re.M)
    ['return f(a, b)']
    """
    # You don't need to edit this function. It's just here to check your work.


def two_of_three(i, j, k):
    """Return m*m + n*n, where m and n are the two smallest members of the
    positive numbers i, j, and k.

    >>> two_of_three(1, 2, 3)
    5
    >>> two_of_three(5, 3, 1)
    10
    >>> two_of_three(10, 2, 8)
    68
    >>> two_of_three(5, 5, 5)
    50
    """
    return i*i + j*j + k*k - max(i,j,k)*max(i,j,k)


def two_of_three_syntax_check():
    """Check that your two_of_three code consists of nothing but a return statement.

    >>> # You aren't expected to understand the code of this test.
    >>> import inspect, ast
    >>> [type(x).__name__ for x in ast.parse(inspect.getsource(two_of_three)).body[0].body]
    ['Expr', 'Return']
    """
    # You don't need to edit this function. It's just here to check your work.


def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    # Hint: To check if b evenly divides a, you can use the expression a % b == 0, which can be read as, "the remainder of dividing a by b is 0."
    # 思路：要求除n外的最大公约数，选择从n-1开始，逐个判断n整除是否为零，当为零时即得到答案
    "*** YOUR CODE HERE ***"
    a = n - 1
    while n % a != 0:
        a = a - 1
    return a


def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    >>> b = hailstone(1)
    1
    >>> b
    1
    """
    "*** YOUR CODE HERE ***"
    # 思路：首先将n与1对比，当不是1时进行hailstone循环，最后输出循环步数
    i = 1
    while n != 1:
        i = i + 1
        print (int(n))
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1
    print (int(n))
    return i