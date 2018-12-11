gs = 300
ser = 4842

def sat(p):
    s = [[]]
    v = 0
    for x in range(gs):
        v += p[0][x]
        init = s[0].append(v)
    v = p[0][0]
    for y in range(1,gs):
        v += p[y][0]
        s.append([v] + [0]*(gs-1))

    for y in range(1, len(p)):
        for x in range(1, len(p[0])):
            s[y][x] = p[y][x] + s[y][x-1] + s[y-1][x] - s[y-1][x-1]
    return s

# make grid
p = []
for x in range(gs):
    p.append([0]*gs)
for y in range(0, len(p)):
    for x in range(0, len(p[0])):
        X = x + 1
        Y = y + 1
        rackid = X + 10
        two = rackid*Y
        three = two + ser
        four = three * rackid
        hundres = int(four / 100) % 10
        final = hundres - 5
        p[y][x] = final

s = sat(p)

mx = 0
# set size to 300 for part 1
for size in range(1,gs):
    print(size)
    for y in range(size,len(p)-size):
        for x in range(size, len(p[0])-size):
            sm  = s[y-size][x-size] \
                - s[y][x-size] \
                - s[y-size][x] \
                + s[y][x]
            if size == 1:
                assert p[y][x] == sm
            p[y][x] = sm

    for y in range(0, len(p)):
        x = p[y].index(max(p[y]))
        if p[y][x] > mx:
            mx = p[y][x]
            X = x+1
            Y = y+1
            S = size

print(X-S+1,Y-S+1,S)
