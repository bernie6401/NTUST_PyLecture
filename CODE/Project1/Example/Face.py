from turtle import *
from Eye import Eye
from Hair import Hair

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
        self.hair = Hair(self) 
        self.leftEye = Eye(self, 'left', eyeColour)
        self.rightEye = Eye(self, 'right', eyeColour)

    def setSize(self, radius):
        self.size = radius

    def getSize(self):
        return self.size

    # Size is normal, large, small
    def setNoseSize(self, size):
        self.noseSize = size

    # Length is short, sholder or long
    def setHairLength(self, length):
        self.hair.setLength(length)

    # Colour is one understand by Python
    def setHairColour(self, c):
        self.hair.setColour(c)

    # Colour is one understand by Python
    def getHairColour(self):
        return self.hair.getColour()

    def draw(self):
        pensize(2)
        self.goHome()
        self.drawOutline()
        self.drawMouth()
        self.drawNose()
        self.leftEye.draw()
        self.rightEye.draw()
        self.hair.draw()

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
        penup()
        right(135)
        forward(self.size/1.7)
        left(90)
        pendown()
        circle(self.size/1.7, 90)
        self.goHome()

    def drawNose(self):
        if self.noseSize == 'large' :
            dot(self.size/2, "grey")
        elif self.noseSize == 'small' :
            dot(self.size/6, "grey")
        else :
            dot(self.size/4, "grey")
        self.goHome()
        



