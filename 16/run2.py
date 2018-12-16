import re

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
possibleValsForOp = []
for i in range(len(ops)):
    possibleValsForOp.append(set(range(len(ops))))

count3 = 0
for i in range(len(f)/4):
    before = map(int, nums.findall(f[i*4 + 0]))
    cmd = map(int, f[i*4 + 1][:-1].split(' '))
    after = map(int, nums.findall(f[i*4 + 2]))

    for op_i, o in enumerate(ops):
        regs = list(before)
        o(regs, cmd[1], cmd[2], cmd[3])
        if regs != after and cmd[0] in possibleValsForOp[op_i]:
            possibleValsForOp[op_i].remove(cmd[0])

print possibleValsForOp
valsForOps = [None]*len(possibleValsForOp)
for j in range(len(valsForOps)):
    for i in range(len(possibleValsForOp)):
        num = len(possibleValsForOp[i])
        if num == 1 and valsForOps[i] is None:
            opCode = list(possibleValsForOp[i])[0]
            valsForOps[i] = opCode
            print valsForOps
            for v in possibleValsForOp:
                if opCode in v:
                    v.remove(opCode)

# Sanity check
for i in range(len(f)/4):
    before = map(int, nums.findall(f[i*4 + 0]))
    cmd = map(int, f[i*4 + 1][:-1].split(' '))
    after = map(int, nums.findall(f[i*4 + 2]))

    v = valsForOps.index(cmd[0])
    op = ops[v]
    op(before, cmd[1], cmd[2], cmd[3])
    print op.__name__, before, after, " - ", cmd
    assert before == after

from random import randint as rand
regs = [0]*4
f2 = [l for l in open('input2.txt')]
for l in f2:
    cmd = map(int, l[:-1].split(' '))
    v = valsForOps.index(cmd[0])
    op = ops[v]
    op(regs, cmd[1], cmd[2], cmd[3])
    print op.__name__, regs, cmd
print regs
