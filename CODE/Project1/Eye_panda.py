from turtle import *

## Exercise 3 Eye Class
## --------------------
## The Eye knows which face it is part of so it can get 
##  the position of the face



class Eye:

    def __init__(self, face, side, colour):
        self.myFace = face
        self.side = side
        self.colour = colour        

    def draw(self):
        penup()
        if self.side == 'left':
            rotation = 115
            setheading(rotation)
            forward(self.myFace.getSize() / 4)
            left(180 - rotation)
            forward(self.myFace.getSize() / 2)
            left(90)
            fillcolor('gray')
            begin_fill()
            pendown()
            circle(self.myFace.getSize() / 3.5)
            end_fill()

            penup()
            left(90)
            forward(self.myFace.getSize() / 5)
            left(90)
            forward(self.myFace.getSize() / 15)
            left(180)
            fillcolor('black')
            begin_fill()
            pendown()        
            circle(self.myFace.getSize() / 8)
            end_fill()

            penup()
            left(90)
            forward(self.myFace.getSize() / 7)
            pendown()
            dot(self.myFace.getSize() / 10, self.colour)
        else:
            rotation = 65
            setheading(rotation)
            forward(self.myFace.getSize() / 4)
            right(rotation)
            forward(self.myFace.getSize() / 2)
            left(90)
            fillcolor('gray')
            begin_fill()
            pendown()
            circle(self.myFace.getSize() / 3.5)
            end_fill()

            penup()
            left(90)
            forward(self.myFace.getSize() / 5)
            right(90)
            forward(self.myFace.getSize() / 15)
            fillcolor('black')
            begin_fill()
            pendown()        
            circle(self.myFace.getSize() / 8)
            end_fill()

            penup()
            left(90)
            forward(self.myFace.getSize() / 7)
            pendown()
            dot(self.myFace.getSize() / 10, self.colour)
        

        penup()
        # left(rotation)
        # forward(self.myFace.getSize() / 6)
        # pendown()
        # left(90)
        # circle(self.myFace.getSize() / 6, 90)
        self.myFace.goHome()

# --------------------------------------------------
#    Functions that are called from with the class
# --------------------------------------------------

