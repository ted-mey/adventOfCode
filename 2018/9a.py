import itertools

class LinkedItem:
    def __init__(self, value, prev, next):
        self.prev = prev
        self.next = next
        self.value = value

def removeMarble(marble):
    marble.prev.next = marble.next
    marble.next.prev = marble.prev

def printLink(curr):
    toPrint = curr.next
    res = []
    res.append(curr.value)
    print("curr:", curr.value)
    while toPrint != curr: 
        res.append(toPrint.value)
        toPrint = toPrint.next
    print(res)

def playMarbles(noPlayers, lastMarbleWorth):
    first = LinkedItem(0, None, None)
    second = LinkedItem(1, first, first)
    first.prev = second
    first.next = second

    result = {}
    i = 2
    curr = second
    highScore = 0
    for player in itertools.cycle(range(noPlayers)): 
        if i % 23 == 0: 
            mToRemove = curr.prev.prev.prev.prev.prev.prev.prev            
            curr = mToRemove.next
            removeMarble(mToRemove)
            marbleScore = i + mToRemove.value
            result[player] = result[player] + marbleScore if player in result else marbleScore
            if result[player] > highScore:
                highScore = result[player]
        else: 
            newItem = LinkedItem(i, curr.next, curr.next.next)
            curr.next.next.prev = newItem
            curr.next.next = newItem
            curr = newItem
        
        #printLink(curr)
        if i == lastMarbleWorth:
            return highScore
        i += 1


#print(playMarbles(10,1618))
#print(playMarbles(13,7999))
#print(playMarbles(17,1104))
print(playMarbles(486,7083300))
