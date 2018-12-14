rec = [3, 7]

elf0 = 0
elf1 = 1
tot = 170641
while len(rec) < tot+10:
    #print ''.join([str(v) for v in rec])
    #print ' '*(elf0) + "0"
    #print ' '*(elf1) + "1"
    #print elf0, elf1

    v = rec[elf0] + rec[elf1]
    if v >= 10:
        rec.append(int(v/10))
    rec.append(v % 10)

    elf0 = (elf0 + rec[elf0] + 1) % len(rec)
    elf1 = (elf1 + rec[elf1] + 1) % len(rec)
print rec
print ''.join([str(v) for v in rec[-10:]])
