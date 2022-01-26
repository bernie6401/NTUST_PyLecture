from turtle import *
from Eye_panda import Eye
from Ear_panda import Ear

## Exercise 3 
## --------------------
## face class using the Eye class
## Position is centre of face
##     Size is radius
##     noseSize - small, normal, large
##     hairColour - any colour
##     hairLength - short, shoulder, long

# A function is defined for each part, with following steps
#    1. pen up
#    2. move to correct position
#    3. pen down
#    4. draw
#    5. return home

class Face:

    def __init__(self, xpos, ypos, eyeColour):
        self.size = 50
        self.coord = (xpos, ypos)
        self.noseSize = 'normal'
        self.ear = Ear(self.size)
        self.leftEye = Eye(self, 'left', eyeColour)
        self.rightEye = Eye(self, 'right', eyeColour)

    def setSize(self, radius):
        self.size = radius

    def getSize(self):
        return self.size

    # Size is normal, large, small
    def setNoseSize(self, size):
        self.noseSize = size
    
    def setEarSize(self, size):
        self.ear.setEarSize(size)

    # EarSize is one understand by Python
    def getEarSize(self):
        return self.ear.getEarSize()

    def draw(self):
        pensize(4)
        self.goHome()
        self.drawOutline()
        self.drawMouth()
        self.drawNose()
        self.leftEye.draw()
        self.rightEye.draw()
        self.ear.setFaceSize(self.size)
        self.ear.draw()

# --------------------------------------------------
#    Functions that are called from with the class
# --------------------------------------------------


    # After drawing each part, turtle position 
    # returns to centre. Parts can be drawn in any order
    def goHome(self):
        penup()
        goto(self.coord)
        setheading(0)
        
    def drawOutline(self):
        penup()
        forward(self.size)
        left(90)
        pendown()
        circle(self.size)
        self.goHome()
        
    def drawMouth(self):
        a = 4
        penup()
        #先定位在臉的下方
        right(90)
        forward(self.size/a)
        left(90)
        
        #再畫出嘴巴
        left(180)
        forward(self.size/a)
        left(90)
        forward(self.size/a)
        left(90)
        pendown()
        circle(self.size/a, 90)
        penup()
        left(180)
        pendown()
        circle(self.size/a, 90)
        self.goHome()

    def drawNose(self):
        a = 4
        penup()
        #要接續嘴巴往上畫鼻子，所以位置要特定
        right(90)
        forward(self.size/a)
        left(90)
        
        #define how big the nose is
        if self.noseSize == 'large' :
            nose_size = 2
        elif self.noseSize == 'small' :
            nose_size = 6
        else :
            nose_size = 4

        #draw nose
        fillcolor('black')
        begin_fill()
        left(60)
        pendown()
        forward(self.size/nose_size)
        left(120)
        forward(self.size/nose_size)
        left(120)
        forward(self.size/nose_size)
        end_fill()
        self.goHome()
        

