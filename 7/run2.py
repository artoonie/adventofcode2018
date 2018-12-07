if False:
    inp = 'tinput.txt'
    add=1
else:
    inp = 'input.txt'
    add=61
lines = [l.split() for l in open(inp)]
lines = [(l[1], l[7]) for l in lines]
lines = [(ord(l[0])-ord('A'), ord(l[1])-ord('A')) for l in lines]
    
graph = []
for i in range(26):
    graph.append([False]*26)

for a,b in lines:
    graph[a][b] = True
# graph[a][b] means b depends on a finishing

def getNumDeps(graph):
    count = []
    for a in range(26):
        curr = 0
        for b in range(26):
            if graph[b][a]:
                curr += 1
        count.append(curr)
    return count

ttc = range(add,add+26)
done = False
order = []
sec = 0
for sec in xrange(9000):
    deps = getNumDeps(graph)
    if all([d == 0 for d in ttc]):
        done = True
    for o in order:
        deps[o] = 1e8
    active = []
    for a,d in enumerate(deps):
        if d == 0:
            active.append(a)
    for a in active:
        ttc[a] -= 1
        if ttc[a] == 0:
            order.append(a)
            for b in range(26):
                graph[a][b] = False
    if done: break
    sec += 1
print sec
