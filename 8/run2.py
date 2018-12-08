nums = [int(x) for x in [l for l in open('input.txt')][0].split(' ')]

valsPerNode = {}
metadataPerNode = {}
childrenPerNode = {}
gIndex = 1
def getNode(nums):
    numChildren = next(nums)
    numMetadata = next(nums)
    global gIndex
    myIndex = gIndex
    gIndex+=1
    sumV = 0
    childrenPerNode[myIndex] = []
    for c in range(numChildren):
        childrenPerNode[myIndex].append(gIndex)
        sumV += getNode(nums)
    metas = []
    for m in range(numMetadata):
        metas.append(next(nums))
    if numChildren == 0:
        metadataPerNode[myIndex] = sum(metas)
    else:
        metadataPerNode[myIndex] = metas
    return sumV

print getNode(iter(nums))

def getVal(m):
    v = metadataPerNode[m]
    if isinstance(v, int):
        #print "Letter ", chr(ord('A')+m-1), "we know to be", v
        return v
    else:
        #print "Letter ", chr(ord('A')+m-1), "has children", [chr(ord('A')+z-1) for z in childrenPerNode[m]]
        sums = 0
        for t in metadataPerNode[m]:
            #print "Letter ", chr(ord('A')+m-1),"is looking for child", t
            if t-1 < len(childrenPerNode[m]):
                sums += getVal(childrenPerNode[m][t-1])
        metadataPerNode[m] = sums
        #print "Letter ", chr(ord('A')+m-1), "is told to be", sums
        return sums

sums = 0
print metadataPerNode
for i in xrange(1, max(metadataPerNode.keys())+1):
    sums += getVal(i)
print metadataPerNode[1]
