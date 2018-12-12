lines = [l for l in open('input.txt')]

initial = lines[0][:-1]
rules = lines[2:]
rules = [r[:-1].split(' => ') for r in rules]
r2 = {}
for r in rules:
    print r[0], "-->", r[1]
    r2[r[0]] = r[1]
print "=="


#v = 20
v = 1000

initial = "."*(v*2) + initial + "."*(v*2)

def count(zero, initial):
    sm = 0
    for i in xrange(len(initial)):
        if initial[i] == '#':
            sm += i - zero
    return sm

last = 0
zero = v*2
for i in xrange(v):
    #for i in xrange(50000000000):
    nextGen = ""
    for j in xrange(len(initial)):
        five = initial[j-2:j+3]
        if five in r2:
            nextGen += r2[five]
        else:
            nextGen += "."
    initial = nextGen

    if i%1==0:
        cnt = count(zero, initial)
        print "At iteration", i+1, "Delta is", (cnt-last), "Resulting in", cnt
        last = cnt
print count(zero, initial)
