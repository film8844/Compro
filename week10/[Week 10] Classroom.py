'''doc'''


def main(num):
    '''main'''
    room = [[int(input()) for _ in range(num)] for _ in range(num)]
    print(room)
    roomc = [[room[j][i] for j in range(num)] for i in range(num)]
    if list(set(map(min, room)).intersection(set(map(max, roomc)))) != []:
        print(list(set(map(min, room)).intersection(set(map(max, roomc))))[0])
    else:
        print("404 Not Found!")


main(int(input()))
