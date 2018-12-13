X_LEFT = 1
X_STRAIGHT = 0
X_RIGHT = -1

D_UP = 0
D_LEFT = 1
D_DOWN = 2
D_RIGHT = 3

class Cart():
    def __init__(self, ch, row, col):
        self.row = row
        self.col = col
        self.nextIntersection = X_LEFT
        self.currDir = list('^<v>').index(ch)
        self.whatWasUnderneath = '|-|-'[self.currDir]
        self.tick = -1

    def step(self, grid, tick):
        if tick == self.tick:
            return # do nothing if we saw it twice

        self.tick = tick
        NEW_DIR = [(-1,0), (0,-1), (1,0), (0,1)]

        grid[self.row][self.col] = self.whatWasUnderneath
        self.row += NEW_DIR[self.currDir][0]
        self.col += NEW_DIR[self.currDir][1]
        self.whatWasUnderneath = grid[self.row][self.col]

        if isinstance(self.whatWasUnderneath, Cart):
            raise Exception("Collision at " + str(self.col) + "," + str(self.row))

        grid[self.row][self.col] = self

        if self.whatWasUnderneath == "+":
            self.currDir = (self.currDir + self.nextIntersection) % 4
            
            self.nextIntersection = (self.nextIntersection - 1)
            if self.nextIntersection == -2:
                self.nextIntersection = 1
        elif self.currDir == D_UP:
            if self.whatWasUnderneath == "|":
                return
            elif self.whatWasUnderneath == "\\":
                self.currDir = D_LEFT
            elif self.whatWasUnderneath == "/":
                self.currDir = D_RIGHT
            else: assert False
        elif self.currDir == D_DOWN:
            if self.whatWasUnderneath == "|":
                return
            elif self.whatWasUnderneath == "\\":
                self.currDir = D_RIGHT
            elif self.whatWasUnderneath == "/":
                self.currDir = D_LEFT
            else:
                print self.whatWasUnderneath, row, col
                assert False
        elif self.currDir == D_RIGHT:
            if self.whatWasUnderneath == "-":
                return
            elif self.whatWasUnderneath == "\\":
                self.currDir = D_DOWN
            elif self.whatWasUnderneath == "/":
                self.currDir = D_UP
            else: assert False
        elif self.currDir == D_LEFT:
            if self.whatWasUnderneath == "-":
                return
            elif self.whatWasUnderneath == "\\":
                self.currDir = D_UP
            elif self.whatWasUnderneath == "/":
                self.currDir = D_DOWN
            else: assert False

    def __repr__(self):
        return list('^<v>')[self.currDir]


def pgrid(l):
    for row in xrange(len(l)):
        print ''.join([str(v) for v in l[row]])

l = [list(v)[:-1] for v in open('input.txt')]
for row in xrange(len(l)):
    for col in xrange(len(l[0])):
        ch = l[row][col]
        if ch in list('^<v>'):
            l[row][col] = Cart(ch, row, col)

for i in xrange(1000):
    # pgrid(l)
    for row in xrange(len(l)):
        for col in xrange(len(l[0])):
            ch = l[row][col]
            if isinstance(ch, Cart):
                ch.step(l, i)
