"""doc"""


def fibo(num):
    """doc"""
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibo(num - 1) + fibo(num - 2)


def main(num):
    """doc"""
    print(fibo(num))


main(int(input()))
