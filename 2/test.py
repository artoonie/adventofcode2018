def countWord(word):
    word = sorted(word)
    currChar = word[0]
    currCount = 1
    two = False
    three = False
    for i,char in enumerate(word[1:]):
        if char == currChar:
            currCount += 1
        if char != currChar or i == len(word)-2:
            if currCount == 2:
                two = True
            if currCount == 3:
                three = True
            currChar = char
            currCount = 1
    return two, three
twos = 0
threes = 0
with open('input.txt', 'r') as f:
    for line in f:
        two, three = countWord(line)
        if two:
            twos += 1
        if three:
            threes += 1
print "Checksum is", twos*threes

minusOneLetter = {}
with open('input.txt', 'r') as f:
    for line in f:
        for ix in xrange(len(line)):
            minusOne = line[:ix] + line[ix+1:]
            if minusOne not in minusOneLetter:
                minusOneLetter[minusOne] = []
            minusOneLetter[minusOne].append(line)

common = ""
for minusOne in minusOneLetter:
    lst = minusOneLetter[minusOne]
    if len(lst) == 2:
        if lst[0] != lst[1]:
            for idx in range(len(lst[0])):
                if lst[0][idx]==lst[1][idx]:
                    common += lst[0][idx]
            break
print "Letters in common:", common
