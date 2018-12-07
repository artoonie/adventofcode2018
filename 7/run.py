lines = [l.split() for l in open('input.txt')]
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

done = False
order = []
while True:
    deps = getNumDeps(graph)
    print deps
    if all([d == 0 for d in deps]):
        done = True
    for o in order:
        deps[o] = 1e8
    toRem = deps.index(0)
    order.append(toRem)
    for b in range(26):
        graph[toRem][b] = False
    if done: break
orderA = ""
for o in order:
    orderA += chr(o + ord('A'))
print orderA
