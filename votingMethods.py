from fileReading import*

#Multiplying 1st choice by 4, 2nd by 3, 3rd by 2, 4th by 1
def bordaCount():
    ranks = combineFile()
    print(ranks)
    for i in range(len(ranks)):
        k=4
        for j in range(len(ranks)):
            ranks[i][j] = ranks[i][j]*k
            k=k-1
    print(ranks)

    finalRanks=[]
    for i in range(len(ranks)):
        sum=0
        for j in range(len(ranks)):
            sum = sum + ranks[i][j]
        finalRanks.append(sum)
    print(finalRanks)

    currMaxIndex = 0
    for i in range(1, 4):
        if finalRanks[i] >= finalRanks[currMaxIndex]:
            currMaxIndex = i

    if currMaxIndex==0:
        return "Tiffany Bond"
    elif currMaxIndex==1:
        return "Jared Forrest Golden"
    elif currMaxIndex==2:
        return "Bruce Poliquin"
    else:
        return "Write-In"

print(bordaCount())