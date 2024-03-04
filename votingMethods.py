## Annika and Dreyenn
## This program calculates the winners based on different voting methods

from fileReading import*


#Multiplying 1st choice by 4, 2nd by 3, 3rd by 2, 4th by 1
def bordaCount():
    ranks = combineFile()
    ##print(ranks)
    for i in range(len(ranks)):
        k=4
        for j in range(len(ranks)):
            ranks[i][j] = ranks[i][j]*k
            k=k-1
    ##print(ranks)

    finalRanks=[]
    for i in range(len(ranks)):
        sum=0
        for j in range(len(ranks)):
            sum = sum + ranks[i][j]
        finalRanks.append(sum)
    ##print(finalRanks)

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


#Just takes into account the number of 1st place rankings
def plurality():
    ranks = combineFile()

    currMaxIndex = 0 
    for i in range(1,4):
        if ranks[i][0] > ranks[currMaxIndex][0]:
            currMaxIndex = i
            
    if currMaxIndex==0:
        return "Tiffany Bond"
    elif currMaxIndex==1:
        return "Jared Forrest Golden"
    elif currMaxIndex==2:
        return "Bruce Poliquin"
    else:
        return "Write-In"
         

# (single transferable vote) (MIGHT NOT INCLUDE BC THIS IS WHAT ACTUALLY HAPPENED)
# (WE ALREADY KNOW WHAT ACTUALLY HAPPENED SO NOT USEFUL)
def rankedChoice():
    ranks = combineFile()
    ranks[0].append("Tiffany Bond")
    ranks[1].append("Jared Forrest Golden")
    ranks[2].append("Bruce Poliquin")
    ranks[3].append("Write In")
    print(ranks)
    
    while len(ranks) > 1: ##while there is more than one candidate remaining
        print(ranks[findMin(ranks)])
        ranks.pop(findMin(ranks))

    return ranks[0]
    

def findMin(ranks):

    currMinIndex = 0
    for i in range(1,len(ranks)):
        if ranks[i][0] < ranks[currMinIndex][0]:
            currMinIndex = i
            
    # 0 is Tiffany Bond, 1 is JF Golden, 2 is Bruce Polquin, 3 is Write in
    return currMinIndex


print(rankedChoice())
#print(plurality())
#print(bordaCount())
