import re


class LinkedPot:
    def __init__(self, prev):
        self.prev = prev
        self.hasPlantGen = {}
        self.next = None


def parseInitialState(input):
    res = re.search("[\#\.]+", input)
    
    input = res.group(0)
    pots = list(input)
    startNode = LinkedPot(None)
    
    next = startNode
    for pot in pots:
        next.hasPlantGen[0] = (True if pot == '#' else False)
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

def buildPotRuleName(pot, gen):
    res = ""
    try:
        res += "#" if pot.prev.prev.hasPlantGen[gen] else "."
    except Exception:
        res += "."
    try:
        res += "#" if pot.prev.hasPlantGen[gen] else "."
    except Exception:
        res += "."
    try:
        res += "#" if pot.hasPlantGen[gen] else "."
    except Exception:
        res += "."
    try:
        res += "#" if pot.next.hasPlantGen[gen] else "."
    except Exception:
        res += "."
    try:
        res += "#" if pot.next.next.hasPlantGen[gen] else "."
    except Exception:
        res += "."
    return res



def step(rules, firstPlant, gen):
    #outFirstPlant = None

    neg2 = LinkedPot(None)
    neg1 = LinkedPot(neg2)
    for g in range(gen+1):
        neg2.hasPlantGen[g] = False
        neg1.hasPlantGen[g] = False
    neg2.next = neg1
    neg1.next = firstPlant
    firstPlant.prev = neg1

    currentPot = neg2
    while(currentPot != None):
        try:
            res = rules[buildPotRuleName(currentPot, gen)]
        except Exception:
            res = False
        currentPot.hasPlantGen[gen+1] = res
#        if outFirstPlant == None and res:
#            outFirstPlant = currentPot
        currentPot = currentPot.next

    return neg2

def calculateScore(startPot, gen):
    score = 0
    index = 0

    currentPot = startPot
    while(currentPot.prev != None):
        currentPot = currentPot.prev
        index -= 1
        print(gen)
        print(currentPot.hasPlantGen)

        if(currentPot.hasPlantGen[gen]):
            score += index
    
    index = 0
    currentPot = startPot
    while(currentPot.next != None):
        index += 1
        currentPot = currentPot.next
        if(currentPot.hasPlantGen[gen]):
            score += index
    return score

def pTree(start, gen):
    print("###Gen", gen)
    n = start
    i = 0
    while(n != None):
        if len(n.hasPlantGen) != gen+1:
            print("i:",i)
            print(n.hasPlantGen)
        n = n.next
        i+=1


def main():
    file = open("exData")
    #file = open("12_input")
    numGen = 20
    startNode = parseInitialState(file.readline())
    rules = parseRules(file.readlines())

    firstPlant = startNode #needs tweek

    for gen in range(numGen):
        pTree(firstPlant, gen)
        firstPlant = step(rules, firstPlant, gen)
        
    print(calculateScore(startNode, numGen))


main()



