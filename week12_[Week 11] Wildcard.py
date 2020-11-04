"""whild"""


def wildcard(rang, word):
    """doc"""
    if len(rang[1]) + len(rang[0]) > len(word):
        return "NO"
    if word.find(rang[0]) == 0 and word[::-1].find(rang[1][::-1]) == 0:
        return "YES"
    return "NO"


def main(num, rang):
    """doc"""
    lis = [input() for _ in range(num)]
    print(*list(map(lambda x: wildcard(rang, x), lis)), sep='\n')


main(int(input()), input().split('*'))
