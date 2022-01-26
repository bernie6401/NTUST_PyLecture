from turtle import *
import math

## Exercise 3 Hair Class
## --------------------
## The Hair knows which face it is part of so it can get 
##  the position of the face

class Ear:
    def __init__(self, face_size):
        self.face_size = face_size

    # Length is short, sholder or long
    def setEarSize(self, size):
        self.size = size

    def getEarSize(self):
        return self.size

    def setFaceSize(self, face_size):
        self.face_size = face_size

    def getFaceSize(self):
        return self.face_size

    def draw(self):
        self.drawEar()


# --------------------------------------------------
#    Functions that are called from with the class
# --------------------------------------------------

    def drawEar(self):
        penup()

        #先定位左邊耳朵的位置，並把位置和方向存起來
        left(90)
        forward(self.face_size)
        left(90)
        circle(self.face_size, 45)
        current_position = position()
        current_heading = heading()

        #draw left ear
        lambda_param = 2
        condition = True
        dist_old = math.inf
        while condition == True:
            circle(self.face_size, 0.1)
            posi = position()
            dist_new = abs((self.size / lambda_param)**2 - ((posi[0] - current_position[0])**2 + (posi[1] - current_position[1])**2))
            if dist_old < dist_new:
                condition = False
                now_heading = heading()
            dist_old = dist_new
        angle = 180 - abs(current_heading - now_heading) * 2
        left(90)
        circle(self.size / lambda_param, angle)
        fillcolor('gray')
        begin_fill()
        pendown()
        circle(self.size / lambda_param, 360 - angle)
        end_fill()

        #定位在原位
        penup()
        goto(current_position)
        setheading(current_heading)

        #再畫外圈
        lambda_param = 1.5
        condition = True
        dist_old = math.inf
        while condition == True:
            circle(self.face_size, 0.1)
            posi = position()
            dist_new = abs((self.size / lambda_param)**2 - ((posi[0] - current_position[0])**2 + (posi[1] - current_position[1])**2))
            if dist_old < dist_new:
                condition = False
                now_heading = heading()
            dist_old = dist_new
        angle = 180 - abs(current_heading - now_heading) * 2
        left(90)
        circle(self.size / lambda_param, angle)
        pendown()
        circle(self.size / lambda_param, 360 - angle)


        #定位在右邊的耳朵原點
        penup()
        goto(current_position)
        setheading(current_heading)
        circle(self.face_size, 270)
        current_position = position()
        current_heading = heading()


        #draw right ear
        lambda_param = 2
        condition = True
        dist_old = math.inf
        while condition == True:
            circle(self.face_size, 0.1)
            posi = position()
            dist_new = abs((self.size / lambda_param)**2 - ((posi[0] - current_position[0])**2 + (posi[1] - current_position[1])**2))
            if dist_old < dist_new:
                condition = False
                now_heading = heading()
            dist_old = dist_new
        angle = 180 - abs(current_heading - now_heading) * 2
        circle(self.face_size, 360 - abs(current_heading - now_heading) * 2)
        right(90)
        fillcolor('gray')
        begin_fill()
        pendown()
        circle(self.size / lambda_param, 360 - angle)
        end_fill()

        #定位在原位
        penup()
        goto(current_position)
        setheading(current_heading)

        #再畫外圈
        lambda_param = 1.5
        condition = True
        dist_old = math.inf
        while condition == True:
            circle(self.face_size, 0.1)
            posi = position()
            dist_new = abs((self.size / lambda_param)**2 - ((posi[0] - current_position[0])**2 + (posi[1] - current_position[1])**2))
            if dist_old < dist_new:
                condition = False
                now_heading = heading()
            dist_old = dist_new
        angle = 180 - abs(current_heading - now_heading) * 2
        circle(self.face_size, 360 - abs(current_heading - now_heading) * 2)
        right(90)
        pendown()
        circle(self.size / lambda_param, 360 - angle)