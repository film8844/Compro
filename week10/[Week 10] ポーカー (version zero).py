"""doc """


def to_num(card):
    """num"""
    if card[0].isdigit():
        return int(card[0])
    else:
        nums = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, "A": 14}
        if card[0] in nums:
            return nums[card[0]]


def staight(nlis):
    """rank"""
    nlis.sort()
    for i in range(5):
        if nlis[0] + i != nlis[i]:
            return False
    return True


def flush(dok):
    """rank"""
    if len(list(set(dok))) == 1:
        return True
    return False


def four(nlis):
    """rank"""
    # if len(list(set(nlis))) == 2:
    #     if max([nlis.count(i) for i in list(set(nlis))]) == 4:
    #         return True
    # return False

    a = list(set(nlis))
    if len(a) == 2:
        liszz =[]
        for i in a:
            liszz.append(nlis.count(i))
        if max(liszz)==4:
            return True
    return False


def full_house(nlis):
    """rank"""
    if len(list(set(nlis))) == 2:
        if max([nlis.count(i) for i in list(set(nlis))]) == 3:
            return True
    return False


def three(nlis):
    """rank"""
    if len(list(set(nlis))) == 3:
        if max([nlis.count(i) for i in list(set(nlis))]) == 3:
            return True
    return False


def two_pair(nlis):
    """rank"""
    if len(list(set(nlis))) == 3:
        if max([nlis.count(i) for i in list(set(nlis))]) == 2:
            return True
    return False


def pair(nlis):
    """rank"""
    if len(list(set(nlis))) == 4:
        return True
    return False


def winner(rank, nlis):
    """win"""

    if rank[0] != rank[1]:
        print("Player", rank.index(max(rank)) + 1)

    else:
        if sum(nlis[0]) > sum(nlis[1]):
            print("Player 1")
        else:
            print("Player 2")


def main():
    """ doc """
    lis, rank, dok, nlis = [], [], [], []
    for i in range(2):
        lis.append(input().replace(',', '').replace("'", '')[1:-1].split(' '))
        rank.append(0)
        dok.append(list(map(lambda x: x[1], lis[i])))
        nlis.append(list(map(to_num, lis[i])))
    for i in range(2):
        if staight(nlis[i]) and flush(dok[i]):
            rank[i] = 9
        elif four(nlis[i]):
            rank[i] = 8
        elif full_house(nlis[i]):
            rank[i] = 7
        elif flush(dok[i]):
            rank[i] = 6
        elif staight(nlis[i]):
            rank[i] = 5
        elif three(nlis[i]):
            rank[i] = 4
        elif two_pair(nlis[i]):
            rank[i] = 3
        elif pair(nlis[i]):
            rank[i] = 2
        else:
            rank[i] = 1
            nlis[i] = [max(nlis)]
    winner(rank, nlis)


main()
