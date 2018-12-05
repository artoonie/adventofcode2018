with open('input.txt') as f:
    for line in f:
        pass

def thing(line):
    line = line.strip('\n')
    i = 0
    while i < len(line)-1:
        curr = line[i]
        next = line[i+1]
        if curr != next and curr.upper() == next.upper():
            before = line[:i]
            after = line[i+2:]
            line = before + after
            i -= 1
            i = max(0, i)
        else:
            i += 1
    return len(line)

print "Len",  thing(line)
vals = {}
for ch in 'abcdefghijklmnopqrstuvwxyz':
    t = line.replace(ch, '')
    t = t.replace(ch.upper(), '')
    l = thing(t)
    vals[ch] = l

m = min(vals.values())
print "max val if you remove one char is", m
