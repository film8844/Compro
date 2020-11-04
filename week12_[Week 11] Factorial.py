"""doc"""


def fac(num):
    """doc"""
    if num == 2:
        return 2
    elif num == 0:
        return 1
    elif num < 0:
        return 0
    else:
        return num * fac(num - 1)


def main(num):
    """doc"""
    print(fac(num))


main(int(input()))
