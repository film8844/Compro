"""doc"""


def check(num):
    """doc"""
    sixx = num - 6
    nine = num - 9
    twen = num - 20
    if sixx == 0:
        return True
    elif nine == 0:
        return True
    elif twen == 0:
        return True
    elif sixx < 0:
        return False
    return check(sixx) or check(nine) or check(twen)


def run():
    """doc"""
    num = int(input())
    cout = 0
    for i in range(num + 1):
        if check(i):
            print(i)
            cout = 1
    if cout == 0:
        print("no")


run()
