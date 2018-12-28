from collections import Counter

rows = open("2a_input").readlines()
twos = 0
threes = 0
for row in rows:
    rowRes = Counter(list(row))    
    twoFound = False
    threeFound = False
    for r in rowRes:        
        if rowRes[r] == 2:
            if(not twoFound):
                twos += 1
                twoFound = True
        elif rowRes[r] == 3:
            if(not threeFound):
                threeFound = True
                threes += 1


print("2: ", twos)
print("3: ", threes)
print(twos * threes)