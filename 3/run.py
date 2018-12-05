claims = {}
with open('input.txt', 'r') as f:
    for line in f:
        claim,at,where,size = line.split(' ')
        left,top = where.split(',')
        top = top[:-1] # remove ":"
        width,height = size.split('x')
        left = int(left)
        top = int(top)
        width = int(width)
        height = int(height)
        claims[claim] = (left, top, width, height)

d = {}
for claim in claims:
    left, top, width, height = claims[claim]
    for x in xrange(left, left+width):
        for y in xrange(top, top+height):
            if (x,y) not in d:
                d[(x,y)] = 0
            d[(x,y)] += 1
count = 0
for loc in d:
    if d[loc] > 1:
        count += 1
print "Total overlapping squares:", count

for claim in claims:
    left, top, width, height = claims[claim]
    br = False
    for x in xrange(left, left+width):
        for y in xrange(top, top+height):
            if d[(x,y)] != 1:
                br = True
                break
        if br:
            break
    if not br:
        print "Doesn't overlap at all", claim
