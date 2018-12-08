nums = [int(x) for x in [l for l in open('input.txt')][0].split(' ')]

def getNode(nums):
    numChildren = next(nums)
    numMetadata = next(nums)
    sumV = 0
    for c in range(numChildren):
        sumV += getNode(nums)
    for m in range(numMetadata):
        v = next(nums)
        sumV += v
    return sumV

print getNode(iter(nums))
