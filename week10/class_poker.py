"""doc"""


class Poker:
    """Pkoer"""
    def to_num(self):
        """point"""
        lis = []
        for i in range(5):
            if self.cards[i][0].isdigit():
                lis.append(int(self.cards[i][0]))
            else:
                nums = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, "A": 14}
                lis.append(nums[self.cards[i][0]])
        return lis
    def dokf(self):
        """dok"""
        return list(map(lambda x: x[1], self.cards))
    def staight(self):
        """rank"""
        self.point.sort()
        for i in range(5):
            if self.point[0] + i != self.point[i]:
                return False
        return True
    def flush(self):
        """rank"""
        if len(list(set(self.dok))) == 1:
            return True
        return False
    def four(self):
        """rank"""
        if len(list(set(self.point))) == 2:
            if max([self.point.count(i) for i in list(set(self.point))]) == 4:
                return True
        return False
    def full_house(self):
        """rank"""
        if len(list(set(self.point))) == 2:
            if max([self.point.count(i) for i in list(set(self.point))]) == 3:
                return True
        return False
    def three(self):
        """rank"""
        if len(list(set(self.point))) == 3:
            if max([self.point.count(i) for i in list(set(self.point))]) == 3:
                return True
        return False
    def two_pair(self):
        """rank"""
        if len(list(set(self.point))) == 3:
            if max([self.point.count(i) for i in list(set(self.point))]) == 2:
                return True
        return False
    def pair(self):
        """rank"""
        if len(list(set(self.point))) == 4:
            return True
        return False
    def rank(self):
        """rank"""
        for _ in range(2):
            if self.staight() and self.flush():
                tmp = 9
            elif self.four():
                tmp = 8
            elif self.full_house():
                tmp = 7
            elif self.flush():
                return 6
            elif self.staight():
                return 5
            elif self.three():
                return 4
            elif self.two_pair():
                return 3
            elif self.pair():
                return 2
            else:
                self.point = [max(self.point)]
                return 1
        return tmp
    def __init__(self, lis):
        """init"""
        self.cards = lis.replace(',', '').replace("'", '')[1:-1].split(' ')
        self.point = self.to_num()
        self.dok = self.dokf()

def main(player):
    """main"""
    for _ in range(2):
        player.append(Poker(input()))
    print("Player", [2, 1][player[0].rank() > player[1].rank()])


main([])
