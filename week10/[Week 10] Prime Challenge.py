"""doc"""


def run(num):
    """doc"""
    if num < 2:
        return print(0)
    lekkii = [True] * (num // 2)
    print(lekkii)
    for i in range(3, int(num ** 0.5) + 1, 2):
        print(lekkii)
        if lekkii[i // 2]:
            lekkii[(i // 2) + i::i] = [False] * len(lekkii[(i // 2) + i::i])
        print(lekkii)
    print(lekkii.count(1))


run(int(input()))
