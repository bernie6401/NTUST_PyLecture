from turtle import *
from Face_panda import Face

## Exercise 1
## ----------
## Simple drawing

# sets the animation speed: can be 'slow'
speed('fast')

# uncomment this to hide the turtle
# hideturtle()

# uncomment for instanteneous drawing - no animation
tracer(0)

#  start of drawing code
f1 = Face(-200, 0, 'white')
f1.setSize(100)
f1.setEarSize(50)
f1.setNoseSize('small')
f1.draw()


f2 = Face(100, 0, 'white')
f2.setSize(200)
f2.setEarSize(100)
f2.setNoseSize('normal')
f2.draw()

f3 = Face(350, 0, 'black')
f3.setSize(50)
f3.setEarSize(10)
f3.setNoseSize('large')
f3.draw()

showturtle()
done()