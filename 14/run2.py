rec = [3, 7]

elf0 = 0
elf1 = 1
tot = "170641"
#tot = "59414"
#tot = "92510"
num = len(tot)
tot = int(tot)
tic = 0
while True:
    v = rec[elf0] + rec[elf1]
    if v >= 10:
        rec.append(int(v/10))
    rec.append(v % 10)

    elf0 = (elf0 + rec[elf0] + 1) % len(rec)
    elf1 = (elf1 + rec[elf1] + 1) % len(rec)
    if rec[-1] == 1 and rec[-2] == 4 and rec[-3] == 6 and rec[-4] == 0 and rec[-5] == 7 and rec[-6] == 1:
    #if rec[-1] == 4 and rec[-2] == 1 and rec[-3] == 4 and rec[-4] == 9 and rec[-5] == 5:
    #f = int(''.join([str(v) for v in rec[-num:]]))
    #if f == tot:
        print len(rec)-num
        break
    tic += 1
