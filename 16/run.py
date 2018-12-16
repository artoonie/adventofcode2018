import re

regs = []
def addr(regs, a, b, c):
    regs[c] = regs[a] + regs[b]
def addi(regs, a, b, c):
    regs[c] = regs[a] + b
def mulr(regs, a, b, c):
    regs[c] = regs[a] * regs[b]
def muli(regs, a, b, c):
    regs[c] = regs[a] * b
def banr(regs, a, b, c):
    regs[c] = regs[a] & regs[b]
def bani(regs, a, b, c):
    regs[c] = regs[a] & b
def borr(regs, a, b, c):
    regs[c] = regs[a] | regs[b]
def bori(regs, a, b, c):
    regs[c] = regs[a] | b
def setr(regs, a, b, c):
    regs[c] = regs[a]
def seti(regs, a, b, c):
    regs[c] = a
def gtir(regs, a, b, c):
    regs[c] = 1 if a > regs[b] else 0
def gtri(regs, a, b, c):
    regs[c] = 1 if regs[a] > b else 0
def gtrr(regs, a, b, c):
    regs[c] = 1 if regs[a] > regs[b] else 0
def eqir(regs, a, b, c):
    regs[c] = 1 if a == regs[b] else 0
def eqri(regs, a, b, c):
    regs[c] = 1 if regs[a] == b else 0
def eqrr(regs, a, b, c):
    regs[c] = 1 if regs[a] == regs[b] else 0


nums = re.compile('\d')
ops = [addr, addi, mulr, muli, banr, bani, borr, bori, setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]
f = [l for l in open('input1.txt')]

count3 = 0
for i in range(len(f)/4):
    before = map(int, nums.findall(f[i*4 + 0]))
    cmd = map(int, f[i*4 + 1][:-1].split(' '))
    after = map(int, nums.findall(f[i*4 + 2]))

    possibleChoices = 0
    for o in ops:
        regs = list(before)
        o(regs, cmd[1], cmd[2], cmd[3])
        if regs == after:
            possibleChoices += 1
    if possibleChoices >= 3:
        count3 += 1

print count3
