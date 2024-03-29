import re


class LinkedPot:
    def __init__(self, prev):
        self.prev = prev
        self.hasPlant = False
        self.next = None
        self.startNode = False


def parseInitialState(input):
    res = re.search("[\#\.]+", input)
    
    input = res.group(0)
    pots = list(input)
    startNode = LinkedPot(None)
    startNode.startNode = True
    
    next = startNode
    for pot in pots:
        next.hasPlant = (True if pot == '#' else False)
        n2 = LinkedPot(next)
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
        neg2 = LinkedPot(None)
        neg1 = LinkedPot(neg2)
        neg2.next = neg1
        neg1.next = firstPlant
        firstPlant.prev = neg1
        init = neg2
    elif firstPlant.next.hasPlant:
        neg1 = LinkedPot(None)
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
            next = LinkedPot(None)
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

    startPot = firstPot
    while(not startPot.startNode):
        startPot = startPot.next

    index = 0
    currentPot = startPot
    while currentPot.prev != None:
        currentPot = currentPot.prev
        index -= 1
        if(currentPot.hasPlant):
            score += index
    
    index = 0
    currentPot = startPot
    while currentPot.next != None:
        index += 1
        currentPot = currentPot.next
        if(currentPot.hasPlant):
            score += index
    return score

def pTree(start):
    n = start
    res = ""
    while(n != None):
        res += "#" if n.hasPlant else "."
        n = n.next
    print(res)

def main():
    file = open("12_input")
    numGen = 20
    firstPlant = parseInitialState(file.readline())
    rules = parseRules(file.readlines())

    for _ in range(numGen):
        pTree(firstPlant)        
        firstPlant = step(rules, firstPlant)

    pTree(firstPlant)        
    print(calculateScore(firstPlant))


main()



