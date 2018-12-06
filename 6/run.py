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
        minDist = min(dists)
        if dists.count(minDist) > 1:
            grid[a][b] = -100
        else:
            grid[a][b] = dists.index(minDist)

invalidSet = set()
for a in xrange(maxX):
    invalidSet.add(grid[a][0])
    invalidSet.add(grid[a][maxY-1])
for b in xrange(maxY):
    invalidSet.add(grid[0][b])
    invalidSet.add(grid[maxX-1][b])

#print "hm"
#for g in grid: print g
print "inv", invalidSet
counts = {}
for a in xrange(maxX):
    for b in xrange(maxY):
        if grid[a][b] in invalidSet: continue
        if grid[a][b] not in counts:
            counts[grid[a][b]] = 0
        counts[grid[a][b]] += 1

print counts
print max(counts.values())
