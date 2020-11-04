"""doc"""
import math


def distand(start, position):
    """doc"""
    lat1 = (start[0] * 3.1416) / 180
    lon1 = (start[1] * 3.1416) / 180
    lat2 = (position[0] * 3.1416) / 180
    lon2 = (position[1] * 3.1416) / 180
    r_world = 6378.137
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    fist_step = (math.sin(dlat / 2) ** 2) + math.cos(lat1) \
                * math.cos(lat2) * (math.sin(dlon / 2) ** 2)
    second_step = 2 * math.asin(math.sqrt(fist_step))
    distance = r_world * second_step
    print("Distance: %.2fkm " % distance, end='')
    direct = ''
    if start[0] - position[0] > 0:
        direct += 'S'
    elif start[0] - position[0] < 0:
        direct += 'N'
    if start[1] - position[1] > 0:
        direct += 'W'
    elif start[1] - position[1] < 0:
        direct += 'E'

    print("Direction:", direct)


def main(num):
    """doc"""
    start = list(map(float, input()[1:-1].replace(',', '').split(' ')))
    position = [list(map(float, input()[1:-1].replace(',', '').split(' '))) for _ in range(num)]
    print("#%d " % (1), end='')
    distand(start, position[0])
    for i in range(1, num):
        print("#%d " % (i + 1), end='')
        distand(position[i - 1], position[i])


main(int(input()))
