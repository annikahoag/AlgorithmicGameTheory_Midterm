## Annika and Dreyenn
## This program calculates the winners based on different voting methods
from fileReading import*


#Multiplying 1st choice by 4, 2nd by 3, 3rd by 2, 4th by 1
def bordaCount():
    ranks = combineFile() #get data
    
    for i in range(len(ranks)): #go thru each ranking
        k=4
        for j in range(len(ranks)): #go thru each rank within this ranking
            ranks[i][j] = ranks[i][j]*k #multiply by number based on rank
            k=k-1 #change k to right number
   

    finalRanks=[] 
    for i in range(len(ranks)): #for each rankings
        sum=0
        for j in range(len(ranks)): 
            sum = sum + ranks[i][j] 
        finalRanks.append(sum)
    

    return ranks,finalRanks


def bordaHelper(finalRanks):
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
    ranks = combineFile() #get array of rankings

    currMaxIndex = 0 
    for i in range(1,4): #loop thru each candidate
        if ranks[i][0] > ranks[currMaxIndex][0]:  #see which has more 1st places 
            currMaxIndex = i
            
    if currMaxIndex==0:
        return "Tiffany Bond"
    elif currMaxIndex==1:
        return "Jared Forrest Golden"
    elif currMaxIndex==2:
        return "Bruce Poliquin"
    else:
        return "Write-In"


#function that will help create the bar graph for plurality by returning the
# number of first place votes each candidate has
def pluralityGraphHelper():
    array = combineFile() #get array
    tbNum = array[0][0] #tiffany bonds number of first place rankings
    jgNum = array[1][0] #same thing for the rest of the candidates
    bpNum = array[2][0]

    #now make it a number that the bar graph in the GUI can handle
    # (make it smaller because right now it would be wayyyy to many pixels)
    tbNum = tbNum/1000
    jgNum = jgNum/1000
    bpNum = bpNum/1000
    return tbNum, jgNum, bpNum

print(pluralityGraphHelper())
    
         

# (single transferable vote) (MIGHT NOT INCLUDE BC THIS IS WHAT ACTUALLY HAPPENED)
# (WE ALREADY KNOW WHAT ACTUALLY HAPPENED SO NOT USEFUL)
def rankedChoice():
    ranks = combineFile()
    ranks[0].append("Tiffany Bond")
    ranks[1].append("Jared Forrest Golden")
    ranks[2].append("Bruce Poliquin")
    ranks[3].append("Write In")
   # print(ranks)
    
    while len(ranks) > 1: ##while there is more than one candidate remaining
        #print(ranks[findMin(ranks)])
        ranks.pop(findMin(ranks))
    return ranks[0]
    

# function that finds the minimum of the first column
def findMin(ranks):
    currMinIndex = 0
    for i in range(1,len(ranks)):
        if ranks[i][0] < ranks[currMinIndex][0]:
            currMinIndex = i
    # 0 is Tiffany Bond, 1 is JF Golden, 2 is Bruce Polquin, 3 is Write in
    return currMinIndex


# copelandddddd
##def copeLand():
##    rankings, numRankings = getTheRankings(giantFileMaker())
##    #first, golden vs bond
##    #second, golden vs poliquin
##    #third, bond vs poliquin
##    for i in range(len(rankings)):


#print(rankedChoice())
#print(plurality())

#print(bordaCount())
