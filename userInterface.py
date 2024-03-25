## User Interface for Midterm
## COM313
## Annika and Dreyenn
from graphics import *
from buttonClass import *
from votingMethods import *


def main():
    #setting up window
    win = GraphWin("Maine's 2022 STV Congressional Election",1000,700)
    win.setBackground("cadetblue1")
    intro = "This program takes every voter's ranking from the 2022 Maine Congressional Election and calculates the winner for each different voting method."
    text = Text(Point(500,100),intro)
    text.setSize(16)
    text.draw(win)
    rButton = Button(win, Point(500,350),100,50,"Show me results!","Red")
    qButton = Button(win,Point(500,650),80,40,"Quit","Grey")


    #get click from user
    pt = win.getMouse()
    while qButton.isClicked(pt) != True: #while user does not quit:
        if rButton.isClicked(pt): #if user chooses to see results:
            text.undraw()
            rButton.unDraw()
            graphs(win)
            realButton = Button(win,Point(500,500),200,50,"See Actual Results... (STV)","White")
            pt = win.getMouse()
            if realButton.isClicked(pt):
                realWin = GraphWin("Real Results!",1400,800)
                img1 = Image(Point(700,200),"round1STV.png")
                img1label = Text(Point(50,200),"Round \n 1")
                img1label.setSize(18)
                img2 = Image(Point(700,600),"round2STV.png")
                img2label = Text(Point(50,600),"Round \n 2")
                img2label.setSize(18)
                img1.draw(realWin)
                img1label.draw(realWin)
                img2.draw(realWin)
                img2label.draw(realWin)
        pt = win.getMouse()  #get another user click


    win.close()



def graphs(window):
    bordaArray,totArray = bordaCount() #get the data for borda count
    ## BORDA
    bordaText = Text(Point(250,50),"Borda Count")
    bordaText.draw(window)
    bWinner = Text(Point(250,75),"The Winner is "+bordaHelper(bordaArray))
    bWinner.draw(window)
    #table:
    #row labels:
    tbRow = Rectangle(Point(50,120),Point(100,145)) #bond
    tbBlabel = Text(Point(75,132.5),"Bond")
    tbRow.draw(window)
    tbBlabel.draw(window)

    jgRow = Rectangle(Point(50,145),Point(100,170)) #golden
    jgBlabel = Text(Point(75,157.5),"Golden")
    jgRow.draw(window)
    jgBlabel.draw(window)

    bpRow = Rectangle(Point(50,170),Point(100,195)) #poliquin
    bpBlabel = Text(Point(75,182.5),"Poliquin")
    bpRow.draw(window)
    bpBlabel.draw(window)

    wiRow = Rectangle(Point(50,195),Point(100,220)) #write in
    wiBlabel = Text(Point(75,207.5),"Write In")
    wiRow.draw(window)
    wiBlabel.draw(window)

    #column labels:
    column1 = Rectangle(Point(100,120),Point(150,100))
    column1label = Text(Point(125,110),"1st (* 4)")
    column1.draw(window)
    column1label.draw(window)

    column2 = Rectangle(Point(150,120),Point(200,100))
    column2label = Text(Point(175,110),"2nd (* 3)")
    column2.draw(window)
    column2label.draw(window)

    column3 = Rectangle(Point(200,120),Point(250,100))
    column3label = Text(Point(225,110),"3rd (* 2)")
    column3.draw(window)
    column3label.draw(window)

    column4 = Rectangle(Point(250,120),Point(300,100))
    column4label = Text(Point(275,110),"4th (* 1)")
    column4.draw(window)
    column4label.draw(window)

    totalColumn = Rectangle(Point(300,120),Point(350,100))
    totalColumnLabel = Text(Point(325,110),"Total")
    totalColumn.draw(window)
    totalColumnLabel.draw(window)

    #actual table numbers
    y = 120
    for i in range(len(bordaArray)):
        x = 100
        y = y+25
        for j in range(len(bordaArray)):
             rect = Rectangle(Point(x,y),Point(x+50,y-25))
             rect.draw(window)
             rectLabel = Text(Point(x+25,y-12.5),bordaArray[i][j])
             rectLabel.draw(window)
             x = x+50

    y = 145
    print(totArray)
    for i in range(len(totArray)):
        rect = Rectangle(Point(300,y),Point(350,y-25))
        rect.draw(window)
        rectLabel = Text(Point(325,y-12.5),totArray[i])
        rectLabel.draw(window)
        y = y+25

    # visual graph <3
    bondBlabel = Text(Point(50,270),"Bond")
    bondBbar = Rectangle(Point(75,265),Point(75+(totArray[0]/5000),275))
    bondBbar.setFill("Green")
    bondBlabel.draw(window)
    bondBbar.draw(window)

    goldenBlabel = Text(Point(50,310),"Golden")
    goldenBbar = Rectangle(Point(75,305),Point(75+(totArray[1]/5000),315))
    goldenBbar.setFill("Blue")
    goldenBlabel.draw(window)
    goldenBbar.draw(window)
    

    poliquinBlabel = Text(Point(50,350),"Poliquin")
    poliquinBbar = Rectangle(Point(75,345),Point(75+(totArray[2]/5000),355))
    poliquinBbar.setFill("Red")
    poliquinBlabel.draw(window)
    poliquinBbar.draw(window)
    
           



    ## PLURALITY
    tbNum, jgNum, bpNum = pluralityGraphHelper() #get num for size of each bar
    #label the graph/section
    pluralText = Text(Point(750,50),"Plurality")
    pluralText.draw(window)
    pWinner = Text(Point(750,75),"The Winner is "+plurality())
    pWinner.draw(window) 
    #graph:
    # 1. label the candidates' bars
    bpNumStr = str(int((bpNum*1000))) #bruce poliquin
    bpPlabel = Text(Point(650,275),"Poliquin")
    bpNumlabel = Text(Point(650,290),bpNumStr+" votes")
    bpPlabel.draw(window)
    bpNumlabel.draw(window)

    jgNumStr = str(int(jgNum*1000)) #jared golden
    jgPlabel = Text(Point(750,275),"Golden")
    jgNumlabel = Text(Point(750,290),jgNumStr+" votes")
    jgPlabel.draw(window)
    jgNumlabel.draw(window)

    tbNumStr = str(int(tbNum*1000)) #tiffany bond
    tbPlabel = Text(Point(850,275),"Bond")
    tbNumlabel = Text(Point(850,290), tbNumStr+" votes")
    tbPlabel.draw(window)
    tbNumlabel.draw(window)
    
    # 2. bar graph
    #draw each bar
    tbPbar = Rectangle(Point(845,265),Point(855,265-tbNum)) #tiffany bond
    tbPbar.setFill("Green")
    tbPbar.draw(window)

    jgPbar = Rectangle(Point(745,265),Point(755,265-jgNum)) #jared golden
    jgPbar.setFill("Blue")
    jgPbar.draw(window)
    
    bpPbar = Rectangle(Point(645,265),Point(655,265-bpNum)) #bruce poliquin
    bpPbar.setFill("Red")
    bpPbar.draw(window)

    

    ## STV (what actually happened)
##    stvText = Text(Point(250,400),"Real Results (STV)")
##    stvText.draw(window)
##    stvWinner = Text(Point(250,425),"The Winner is Jared Forrest Golden")
##    stvWinner.draw(window)
    

main()
