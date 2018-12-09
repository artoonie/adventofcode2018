class Mbls():
    def __init__(self):
        self.start = 0
        self.v = 1000
        self.l = [None]*self.v

    def at(self,idx):
        return self.l[idx-self.start]

    def _ref(self):
        self.start += 1
        self.l = self.l[1:]
        self.l.append(None)

    def put(self,idx, v):
        if(idx>self.v):
            self._ref()
        print(idx, self.start)
        print(len(self.l))
        self.l[idx-self.start] = v

    def pop(self,idx):
        v= self.l.pop(idx-self.start)
        self.l.append(None)
        return v

lines = [l for l in open('input.txt')]
print(lines)
numPlayers = 430
lastMarble  = 71588*100
#numPlayers = 10
#lastMarble  = 1618
mbls = [0,1]

def cw(i):
    return (i+1) % (len(mbls))

score = {}
for i in range(numPlayers):
    score[i] = 0

currPlayer = 2
currMbl_i = 1
for marble_i in range(2,lastMarble):
    #print(mbls)
    #print(currMbl_i)
    if marble_i % 23 != 0:
        nx = cw(currMbl_i+1)
        if nx == 0:
            mbls.append(marble_i)
            currMbl_i = len(mbls)-1
        else:
            mbls.insert(nx, marble_i)
            currMbl_i = nx
    else:
        score[currPlayer] += marble_i
        min7 = (currMbl_i - 7) % len(mbls)
        score[currPlayer] += mbls.pop(min7)
        currMbl_i = min7
    currPlayer += 1
    currPlayer = currPlayer % numPlayers
print("MARB",mbls)

# lol below this is a trash attempt at part 2
mbls2 = Mbls()
for i,m in enumerate(mbls):
    mbls2.put(i,m)

for marble_i in range(101,lastMarble):
    #print(mbls)
    #print(currMbl_i)
    if marble_i % 23 != 0:
        nx = cw(currMbl_i+1)
        mbls2.put(nx, marble_i)
        currMbl_i = nx
    else:
        score[currPlayer] += marble_i
        min7 = (currMbl_i - 7)
        print(min7)
        score[currPlayer] += mbls2.pop(min7)
        currMbl_i = min7
    currPlayer += 1
    currPlayer = currPlayer % numPlayers


print(max(score.values()))
