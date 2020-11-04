"""doc"""


class CaSino:
    """My base class."""

    def term(self):
        """doc"""
        return self.center

    def move(self, swap):
        """move"""
        if swap == 'A':
            self.left, self.center = self.center, self.left
        elif swap == 'B':
            self.right, self.center = self.center, self.right
        elif swap == 'C':
            self.left, self.right = self.right, self.left
        return 1

    def noww(self, action):
        """this"""
        for i in action:
            self.move(i)
        if self.center:
            return 'C'
        elif self.right:
            return 'R'
        elif self.left:
            return 'L'

    def __init__(self, start, action):
        """start"""
        self.left = False
        self.center = False
        self.right = False
        if start == 'L':
            self.left = True
        elif start == 'C':
            self.center = True
        else:
            self.right = True
        self.now = self.noww(action)
        self.tset = self.term()


def main():
    """main"""

    game = CaSino(input(), list(input()))
    print(game.now)


main()
