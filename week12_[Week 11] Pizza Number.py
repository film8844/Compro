"""doc"""


def check(num):
    """doc"""
    sixx, nine, twen = num - 6, num - 9, num - 20
    if sixx == 0:
        return True
    elif nine == 0:
        return True
    elif twen == 0:
        return True
    elif sixx < 0:
        return False
    return check(sixx) or check(nine) or check(twen)


def run(num, cout=True):
    """doc"""
    for i in range(num + 1):
        if check(i):
            print(i)
            cout = False
    if cout:
        print("no")


run(int(input()))
