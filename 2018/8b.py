import sys


def main():
    def readNode(startIndex):
        noChilds = data[startIndex]
        noDataItems = data[startIndex+1]

        nextStartPos = startIndex+2
        childResults = []

        for _ in range(noChilds):
            child = readNode(nextStartPos)
            nextStartPos = child["nextStartPos"]
            childResults.append(child["result"])

        valueEntries = []
        for _ in range(noDataItems):
            valueEntries.append(data[nextStartPos])
            nextStartPos += 1
        if noChilds == 0:
            return {"nextStartPos": nextStartPos, "result": sum(valueEntries)}
        else:
            res = sum(
                map(lambda x: childResults[x-1] if x <= len(childResults) else 0, valueEntries))
#                map(lambda x: x <= len(childResults) and childResults[x-1] or 0, valueEntries))
            return {
                "nextStartPos": nextStartPos,
                "result": res
            }

    data = list(map(int, open("8a_input").readline().split()))
    print(readNode(0)["result"])


main()
