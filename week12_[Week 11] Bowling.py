"""doc"""


def score(game, i):
    """doc"""
    if game[i].isdigit():
        return int(game[i])
    elif game[i] == 'X':
        return 10
    elif game[i] == '/':
        return 10 - score(game, i - 1)
    return 0


def main(play, tamm=0):
    """doc"""
    last, play = play[-1], ''.join(play)
    for i in range(len(play) - len(last)):
        if play[i] == 'X':
            tamm += score(play, i + 1)
            tamm += score(play, i + 2)
        elif play[i] == '/':
            tamm += score(play, i + 1)
        tamm += score(play, i)
    for i in range(len(last)):
        tamm += score(last, i)
    print(tamm)


main(input().split(' '))
