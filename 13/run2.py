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
        self.dead = False

    def step(self, grid):
        if self.dead: return
        NEW_DIR = [(-1,0), (0,-1), (1,0), (0,1)]

        grid[self.row][self.col] = self.whatWasUnderneath
        self.row += NEW_DIR[self.currDir][0]
        self.col += NEW_DIR[self.currDir][1]
        self.whatWasUnderneath = grid[self.row][self.col]

        if isinstance(self.whatWasUnderneath, Cart):
            assert not isinstance(self.whatWasUnderneath.whatWasUnderneath, Cart)
            print "Killing two carts", self.row, self.col
            grid[self.row][self.col] = self.whatWasUnderneath.whatWasUnderneath
            self.dead = True
            self.whatWasUnderneath.dead = True
            assert self != self.whatWasUnderneath
            return

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
carts = []
for row in xrange(len(l)):
    for col in xrange(len(l[0])):
        ch = l[row][col]
        if ch in list('^<v>'):
            l[row][col] = Cart(ch, row, col)
            carts.append(l[row][col])

for i in xrange(100000):
    carts = [c for c in carts if not c.dead]
    assert len(carts) % 2 == 1
    carts = sorted(carts, key=lambda x: (x.row, x.col))
    if len(carts) <= 1:
        lastCart = carts[0]
        print lastCart.col, lastCart.row
        break
    if i % 100 == 0:
        print i, "num carts", len(carts)

    cartRowCol = None
    # pgrid(l)
    for c in carts:
        c.step(l)
