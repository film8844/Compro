'''doc'''


def main(start_i, start_j):
    '''main'''
    table = [['_' for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            if i == start_i and j == start_j:
                table[i][j] = 'Q'

            elif i - j == start_i - start_j:
                table[i][j] = 'x'

            elif i + j == start_i + start_j:
                table[i][j] = 'x'

            elif i == start_i:
                table[i][j] = 'x'

            elif j == start_j:
                table[i][j] = 'x'
    print(*table,sep="\n")

    print(" _" * 8)
    for i in table:
        print('|', end='')
        for j in i:
            print(j+"|", end='')
        print()


main(int(input()), int(input()))
