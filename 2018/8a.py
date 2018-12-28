import sys


def main():
    def readNode(startIndex):
        noChilds = data[startIndex]
        noDataItems = data[startIndex+1]

        nextStartPos = startIndex+2
        for _ in range(noChilds):
            nextStartPos = readNode(nextStartPos)
        
        nonlocal result
        for _ in range(noDataItems):
            print(data[nextStartPos])
            result += data[nextStartPos]
            nextStartPos += 1
        return nextStartPos

    result = 0
    data = list(map(int, open("8a_input").readline().split()))
    readNode(0)
    print(result)


main()
