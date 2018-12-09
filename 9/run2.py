class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next_node = None
        self.prev_node = None

    def get_data(self):
        return self.data

    def set_next(self, new_next):
        new_next.next_node = self.next_node
        self.next_node.prev_node = new_next
        self.next_node = new_next
        new_next.prev_node = self

    def pop(self):
        p = self.prev_node
        p.next_node = self.next_node
        self.next_node.prev_node = p
        return p.next_node

lines = [l for l in open('input.txt')]
numPlayers = 430
lastMarble  = 71588*100
#numPlayers = 9
#lastMarble  = 27
#numPlayers = 10
#lastMarble  = 1618

first = Node(0)
second = Node(1)
first.next_node = second
first.prev_node = second
second.next_node = first
second.prev_node = first
currNode = second

def pr(first, num):
    for i in range(num):
        print(first.data, end=',')
        first = first.next_node
    print()
def cw(i):
    return (i+1) % (len(mbls))
def back7(node):
    for i in range(7):
        node = node.prev_node
    return node

score = {}
for i in range(numPlayers):
    score[i] = 0

currPlayer = 2
for marble_i in range(2,lastMarble):
    #print(marble_i, end=': ')
    #pr(first, marble_i)
    #print("CURR", currNode.data)
    if marble_i % 23 != 0:
        node = Node(marble_i)
        currNode.next_node.set_next(node)
        currNode = node
    else:
        score[currPlayer] += marble_i
        remNode = back7(currNode)
        score[currPlayer] += remNode.data
        currNode = remNode.pop()
    currPlayer += 1
    currPlayer = currPlayer % numPlayers

print(max(score.values()))
