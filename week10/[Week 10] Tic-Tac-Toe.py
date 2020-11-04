"""doc"""


def table(lis):
    """doc"""
    print("+-+-+-+")
    for i in lis:
        print('|', end="")
        for j in i:
            print("%c|" % j, end="")
        print()
        print("+-+-+-+")


def checkwinner(lis):
    """doc"""
    for i in range(3):
        if lis[i][0] == lis[i][1] == lis[i][2]:
            return True
        elif lis[0][i] == lis[1][i] == lis[2][i]:
            return True
    if lis[0][0] == lis[1][1] == lis[2][2]:
        return True
    elif lis[0][2] == lis[1][1] == lis[2][0]:
        return True
    return False


def run():
    """doc"""
    print("Welcome to OX!")
    print(" ")
    lis = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    table(lis)
    print(" ")
    play = 'X'
    ind = 1
    checl = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    while ind < 10:
        print("It's %c's turn!" % play)
        txt = input("Please enter cell number (1-9) --> ")
        while not txt in checl:
            txt = input("Please enter cell number (1-9) --> ")
        for i in range(3):
            for j in range(3):
                if lis[i][j] == txt:
                    lis[i][j] = play
                    del checl[checl.index(txt)]
                    break
        table(lis)
        print(" ")
        if checkwinner(lis):
            print("The winner is %c!!" % play)
            return 1

        if play == 'X':
            play = 'O'
        else:
            play = 'X'
        ind += 1
    print("Draw!!")


run()

# It's O's turn!
# Please enter cell number (1-9) --> 3
# +-+-+-+
# |1|2|O|
# +-+-+-+
# |4|X|6|
# +-+-+-+
# |7|8|9|
# +-+-+-+
