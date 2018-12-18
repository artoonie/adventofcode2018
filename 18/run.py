g = [[c for c in l[:-1]] for l in open('input.txt')]

def eq(r, c, eq):
    if r < 0: return False
    if c < 0: return False
    if r >= len(g): return False
    if c >= len(g[0]): return False
    return g[r][c] == eq

def neighborsEq(r, c, val):
    count = 0
    if eq(r-1, c, val):
        count+=1
    if eq(r+1, c, val):
        count+=1
    if eq(r, c-1, val):
        count+=1
    if eq(r, c+1, val):
        count+=1
    if eq(r+1, c+1, val):
        count+=1
    if eq(r+1, c-1, val):
        count+=1
    if eq(r-1, c+1, val):
        count+=1
    if eq(r-1, c-1, val):
        count+=1
    return count

def count():
    trees = 0
    lumbs= 0
    for r in range(len(g)):
        for c in range(len(g[0])):
            if g[r][c] == '|':
                trees += 1
            if g[r][c] == '#':
                lumbs += 1
    return trees*lumbs

for i in xrange(1000):
    print i % 28, count()

    toSet = {}
    for r in range(len(g)):
        for c in range(len(g[0])):
            if g[r][c] == '.':
                if neighborsEq(r, c, '|') >= 3:
                    toSet[(r, c)] = '|'
            if g[r][c] == '|':
                if neighborsEq(r, c, '#') >= 3:
                    toSet[(r, c)] = '#'
            if g[r][c] == '#':
                if neighborsEq(r, c, '#') == 0 or neighborsEq(r, c, '|') == 0:
                    toSet[(r, c)] = '.'
    for t in toSet:
        g[t[0]][t[1]] = toSet[t]

# 1000000000 % 28 == 20, so pick the last [20]
