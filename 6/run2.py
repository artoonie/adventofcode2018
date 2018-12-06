x = [l.split(',') for l in open('input.txt')]
x = [(int(v[0]), int(v[1].replace(' ',''))) for v in x]
maxX = max([v[0] for v in x])+1
maxY = max([v[1] for v in x])+1

def dist(a,b):
    return abs(a[0]-b[0]) + abs(a[1] - b[1])

grid = []
for g in range(maxX):
    grid.append([0]*maxY)
for a in xrange(maxX):
    for b in xrange(maxY):
        dists = [dist([a,b], g) for g in x]
        sumDist = sum(dists)
        grid[a][b] = sumDist

s = 0
for a in xrange(maxX):
    for b in xrange(maxY):
        if grid[a][b] < 10000:
            s += 1
print s
