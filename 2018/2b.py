from collections import Counter

def doIt(rows):
    rowLen = len(rows[0])-1
    print("rL", rowLen)
    for i in range(rowLen):
        words = []
        for row in rows:
            split = list(row)
            word = ""
            for j in range(rowLen): 
                word = word + split[j] if j != i else word
            if word in words:
                return word
            else:
                words.append(word)

rows = open("2a_input").readlines()
print(doIt(rows))
