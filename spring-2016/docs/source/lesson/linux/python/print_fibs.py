import sys

def fib(n):
    """
    Return the nth fibonacci number

    The nth fibonacci number is defined as follows:
    Fn = Fn-1 + Fn-2
    F2 = 1
    F1 = 1
    F0 = 0
    """

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


if __name__ == '__main__':
    n = int(sys.argv[1])
    print fib(n)
