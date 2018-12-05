things = []
with open('input.txt') as f:
    currGuard = -1
    for line in f:
        month = line[6:8]
        day = line[9:11]
        hour = line[12:14]
        minute = line[15:17]
        txt = line[19:]
        things.append((int(month), int(day), int(hour), int(minute), txt))
things = sorted(things)
guards = {}

guardid = None
startTime = None
endTime = None
for (month, day, hour, minute, txt) in things:
    if "Guard" in txt:
        guardid = int(txt.split(' ')[1][1:])
    elif "asleep" in txt:
        startTime = minute
    elif "wakes" in txt:
        endTime = minute

        if guardid not in guards:
            guards[guardid] = [0]*60
        for mn in range(startTime, endTime):
            guards[guardid][mn] += 1

maxG = None
maxSum = -1
maxMin = None
for g in guards:
    mins = guards[g]
    sm = sum(mins)
    if sm > maxSum:
        maxSum = sm
        maxMin = mins.index(max(mins))
        maxG = g

print "Guard:", maxG
print "Max minute:", maxMin
print "Mult", maxG*maxMin


biggestMinute = -1
bigMinute = None
bigGuard = None
for g in guards:
    sameMinute = max(guards[g])
    if sameMinute > biggestMinute:
        biggestMinute = sameMinute
        bigMinute = guards[g].index(sameMinute)
        bigGuard = g
print "Guard:", bigGuard
print "Always sleeps at", bigMinute
print "Mult", bigGuard*bigMinute
