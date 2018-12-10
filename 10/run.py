def nxNy(g):
    gridMinX = min([t[0] for t in g])
    gridMinY = min([t[1] for t in g])
    gridMaxX = max([t[0] for t in g])
    gridMaxY = max([t[1] for t in g])
    grid = []
    nX = gridMaxX - gridMinX + 1
    nY = gridMaxY - gridMinY + 1
    return nX, nY, gridMinX, gridMinY

def printGrid(txt, g):
    nX, nY, gridMinX, gridMinY = nxNy(g)
    grid = []
    print(txt)
    for y in range(nX):
        grid.append(['.']*nY)
    for (posx, posy, velx, vely) in g:
        grid[posx-gridMinX][posy-gridMinY] = '#'
    for y in range(nY):
        for x in range(nX):
            print(grid[x][y], end='')
        print()
    return

lines = [l for l in open('input.txt')]
s=[]
for l in lines:
    a = l.replace('<','').replace('>','').split('=')
    posx,posy = a[1].split(',')
    posy = posy.replace(' ','').split('v')[0]

    velx, vely = a[2].split(',')
    posx = int(posx)
    posy = int(posy)
    velx = int(velx)
    vely = int(vely)
    s.append([posx, posy, velx, vely])

lastG = 1e12
for i in range(100000):
    for v in range(len(s)):
        s[v][0] += s[v][2]
        s[v][1] += s[v][3]
    nX, nY, gridMinX, gridMinY = nxNy(s)
    print("Curr grid size:", nX, nY)
    if nX*nY > lastG:
        # rewind
        for v in range(len(s)):
            s[v][0] -= s[v][2]
            s[v][1] -= s[v][3]
        printGrid("after " + str(i) + " seconds", s)
        break
    else:
        lastG = nX*nY
