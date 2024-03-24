#Dreyenn Osgood
#COM110 Final Project
#05/18/2022
#Button Class

from graphics import *
from random import *

#a class that creates a Button object which will be clickable
class Button:
    #constructor method, always first one you write in a class definition
    def __init__(self,win,center,width,height,label,color):
        """Creates a rectangular button where:
            win is the GraphWin where the button will be drawn
            center will be a point object where button is centered
            width is an integer which is width of button in pixels
            height is an interger thts the height of the button in pixels
            label is a string that will appear on the button
            color is the desired color of the button"""
        x,y = center.getX(), center.getY()
        self.xmin = x-width/2 #instance var for left border
        self.xmax = x+width/2 #instance var for right border
        self.ymin = y-height/2 #instance var for top border
        self.ymax = y+height/2 #instance var for bottom border
        pt1 = Point(self.xmin,self.ymin) 
        pt2 = Point(self.xmax,self.ymax) 
        self.rect = Rectangle(pt1,pt2) #instance var creating rectangle
        self.rect.draw(win)
        self.rect.setFill(color)
        self.words = Text(center, label) #instance var for Text/words
        self.words.draw(win)
        self.activate()

    def deactivate(self):
        """sets this button to deactivated so its not clickable"""
        #color text grey
        self.words.setFill("darkgrey")
        #set outline to be thinner
        self.rect.setWidth(1)
        #set the boolean flag self.active to False
        self.active = False

    def activate(self):
        """sets this button to activated, which means it can be clicked"""
        #set color of label to black
        self.words.setFill("black")
        #set outline to look bolder
        self.rect.setWidth(2) #set outline to 2 pixels thick
        #set boolean flag self.active to True
        self.active = True 

    def isClicked(self,pt): #pt is point where user clicks
        """returns True if pt is within boundaries of the button
        False otherwise"""
        #if the button is activated and click is within button boundaries:
        if self.active and \
            pt.getX()>=self.xmin and pt.getX()<= self.xmax and \
            pt.getY()>= self.ymin and pt.getY()<=self.ymax: \
            return True #the button is clicked
        else:
            return False #button is not clicked

    def unDraw(self):
        """makes the button disappear"""
        self.deactivate()
        self.rect.undraw()
        self.words.undraw()

