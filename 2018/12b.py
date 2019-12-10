import re


class LinkedPot:
    def __init__(self, prev, index):
        self.prev = prev
        self.hasPlant = False
        self.next = None
        self.startNode = False
        self.index = index


def parseInitialState(input):
    res = re.search("[\#\.]+", input)
    
    input = res.group(0)
    pots = list(input)
    startNode = LinkedPot(None, 0)
    startNode.startNode = True
    
    next = startNode
    for pot in pots:
        next.hasPlant = (True if pot == '#' else False)
        n2 = LinkedPot(next, next.index+1)
        next.next = n2
        next = n2
    next.prev.next = None
    return startNode

def parseRules(rows):
    rules = {}
    for row in rows:
        res = re.search("([\#\.]{5}).*([\#\.])", row)
        if res != None:
            rules[res.group(1)] = True if res.group(2) == "#" else False
    return rules

def buildPotRuleName(pot):
    res = ""
    try:
        res += "#" if pot.prev.prev.hasPlant else "."
    except Exception:
        res += "."
    try:
        res += "#" if pot.prev.hasPlant else "."
    except Exception:
        res += "."
    try:
        res += "#" if pot.hasPlant else "."
    except Exception:
        res += "."
    try:
        res += "#" if pot.next.hasPlant else "."
    except Exception:
        res += "."
    try:
        res += "#" if pot.next.next.hasPlant else "."
    except Exception:
        res += "."
    return res


def step(rules, firstPlant):
    init = firstPlant
    if firstPlant.hasPlant:
        neg2 = LinkedPot(None, firstPlant.index-2)
        neg1 = LinkedPot(neg2, firstPlant.index-1)
        neg2.next = neg1
        neg1.next = firstPlant
        firstPlant.prev = neg1
        init = neg2
    elif firstPlant.next.hasPlant:
        neg1 = LinkedPot(None, firstPlant.index-1)
        neg1.next = firstPlant
        firstPlant.prev = neg1
        init = neg1
    
    currentPot = init
    while currentPot != None:
        try:
            res = rules[buildPotRuleName(currentPot)]
        except Exception:
            res = False
        currentPot.nextGen = res
        
        if currentPot.next == None and (currentPot.hasPlant or currentPot.prev.hasPlant):
            next = LinkedPot(None, currentPot.index+1)
            currentPot.next = next
            next.prev = currentPot        
        currentPot = currentPot.next

    currentPot = init
    while(currentPot != None):
        currentPot.hasPlant = currentPot.nextGen
        currentPot = currentPot.next

    return init

def calculateScore(firstPot):
    score = 0
    while firstPot.next != None:
        if(firstPot.hasPlant):
            score += firstPot.index
        firstPot = firstPot.next
    return score

def pTree(start):
    n = start
    res = ""
    index = ""
    while(n != None):
        index += str(n.index)
        if n.startNode:
            res += "0"
            n = n.next
            continue
        res += "#" if n.hasPlant else "."
        n = n.next
    print(res)
    print(index)


def clean(start):
    res = start
    reader = start
    i = 0
    while(not reader.hasPlant):
        reader = reader.next
        if i > 4:
            res = res.next
        i += 1
    return res


def main():
    file = open("12_input")
    numGen = 50000
    firstPlant = parseInitialState(file.readline())
    rules = parseRules(file.readlines())

    for num in range(numGen):
        #pTree(firstPlant)
        firstPlant = step(rules, firstPlant)
        if num % 20:
            firstPlant = clean(firstPlant) 

#    pTree(firstPlant)        
    print(calculateScore(firstPlant))


main()



