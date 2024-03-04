def dataReader(fileName):
    with open(fileName) as f:
        #reader = f.read()
        reader = f.readlines()

    #Making delimeter a space instead of a comma
    repl_delim = ' '
    data = []
    for ele in reader:
        data.append(ele.replace(", ", repl_delim))


    #Setting up 2D array
    #Row indices represent T. Bond, J.F. Golden, B. Poliquin, Write-In in that order
    #Column indices represent ranking
    results = []
    for i in range(4):
        col = []
        for j in range(4):
            col.append(0)
        results.append(col)
    #print(results)


    #Removing comma in names
    dataFinal=[]
    for line in data:
        tempLine = line.split(',')
        #tempLine = line.replace('\n', '')
        dataFinal.append(tempLine)
    #print(dataFinal[0][0])
    #print(len(data))

    #for i in range(5):
     #   print(data[i])

    ## 1ST PLACE RANKINGS ##
    #Adding values to 1st column of T. Bond
    bondCounter=0
    for i in range(len(dataFinal)):
        if dataFinal[i][0]=='"Bond Tiffany"':
            bondCounter+=1
            #print(bondCounter)
    results[0][0]=bondCounter

    #Adding values to 1st column of J.F. Golden
    goldenCounter=0
    for i in range(len(dataFinal)):
        if dataFinal[i][0]=='"Golden Jared Forrest"':
            goldenCounter+=1
    results[1][0]=goldenCounter

    #Adding values to 1st column of B. Poliquin
    poliCounter=0
    for i in range(len(dataFinal)):
        if dataFinal[i][0]=='"Poliquin Bruce"':
            poliCounter+=1
    results[2][0]= poliCounter

    #Adding values to 1st column of write-ins
    wiCounter=0
    for i in range(len(dataFinal)):
        if dataFinal[i][0]=='Write-in':
            wiCounter+=1
    results[3][0] = wiCounter



    ## 2ND PLACE RANKINGS ##
    #Adding values to 2nd column of T. Bond
    bondCounter=0
    for i in range(len(dataFinal)):
        if dataFinal[i][1]=='"Bond Tiffany"':
            bondCounter+=1
            #print(bondCounter)
    results[0][1]=bondCounter

    #Adding values to 2nd column of J.F. Golden
    goldenCounter=0
    for i in range(len(dataFinal)):
        if dataFinal[i][1]=='"Golden Jared Forrest"':
            goldenCounter+=1
    results[1][1]=goldenCounter

    #Adding values to 2nd column of B. Poliquin
    poliCounter=0
    for i in range(len(dataFinal)):
        if dataFinal[i][1]=='"Poliquin Bruce"':
            poliCounter+=1
    results[2][1]= poliCounter

    #Adding values to 2nd column of write-ins
    wiCounter=0
    for i in range(len(dataFinal)):
        if dataFinal[i][1]=='Write-in':
            wiCounter+=1
    results[3][1] = wiCounter



    ## 3RD PLACE RANKINGS ##
    #Adding values to 3rd column of T. Bond
    bondCounter=0
    for i in range(len(dataFinal)):
        if dataFinal[i][2]=='"Bond Tiffany"':
            bondCounter+=1
            #print(bondCounter)
    results[0][2]=bondCounter

    #Adding values to 3rd column of J.F. Golden
    goldenCounter=0
    for i in range(len(dataFinal)):
        if dataFinal[i][2]=='"Golden Jared Forrest"':
            goldenCounter+=1
    results[1][2]=goldenCounter

    #Adding values to 3rd column of B. Poliquin
    poliCounter=0
    for i in range(len(dataFinal)):
        if dataFinal[i][2]=='"Poliquin Bruce"':
            poliCounter +=1
    results[2][2]= poliCounter

    #Adding values to 3rd column of write-ins
    wiCounter=0
    for i in range(len(dataFinal)):
        if dataFinal[i][2]=='Write-in':
            wiCounter+=1
    results[3][2] = wiCounter



    ## 4th PLACE RANKINGS ##
    #Adding values to 4th column of T. Bond
    bondCounter=0
    for i in range(len(dataFinal)):
        if dataFinal[i][3]=='"Bond Tiffany"\n':
            bondCounter+=1
            #print(bondCounter)
    results[0][3]=bondCounter

    #Adding values to 4th column of J.F. Golden
    goldenCounter=0
    for i in range(len(dataFinal)):
        if dataFinal[i][3]=='"Golden Jared Forrest"\n':
            goldenCounter+=1
    results[1][3]=goldenCounter

    #Adding values to 4th column of B. Poliquin
    poliCounter=0
    for i in range(len(dataFinal)):
        if dataFinal[i][3]=='"Poliquin Bruce"\n':
            poliCounter+=1
    results[2][3]= poliCounter

    #Adding values to 4th column of write-ins
    wiCounter=0
    for i in range(len(dataFinal)):
        if dataFinal[i][3]=='Write-in\n':
            wiCounter+=1
    results[3][3] = wiCounter

    return results

def adder(mainResult, result2):
    for i in range(0, 4):
        for j in range(0, 4):
            mainResult[i][j] = mainResult[i][j] + result2[i][j]
    return mainResult

def combineFile():
    mainResult = adder(dataReader("reptocongress2-1.csv"), dataReader("reptocongress2-2.csv"))
    mainResult = adder(mainResult, dataReader("reptocongress2-3.csv"))
    mainResult = adder(mainResult, dataReader("reptocongress2-4.csv"))
    mainResult = adder(mainResult, dataReader("reptocongress2-5.csv"))
    mainResult = adder(mainResult, dataReader("reptocongress2-6.csv"))
    mainResult = adder(mainResult, dataReader("reptocongress2-7.csv"))
    return mainResult
