"""doc"""


def main(num):
    """doc"""
    agent = 0
    lis = [0.07, 0.10, 0.15, 0.18, 0.20]
    nummber = [list(range(10, 21)), list(range(21, 31)), list(range(31, 41)), list(range(41, 61))]
    for i in range(len(nummber)):
        if num in nummber[i]:
            agent = lis[i]
    if agent == 0 and num < 10:
        return print("I don't care.")
    elif agent == 0 and num > 60:
        agent = lis[-1]

    print("%.3f" % ((1 - agent) * num))


main(int(input()))
