from turtle import Turtle
import time


p = Turtle()
p.pensize(5)
p.color('purple')
p.speed(1)
p.up()
p.goto(-50, 50)
p.down()
# set the start point
for i in range(4):
    p.forward(100)
    p.right(90)
p.up()
p.goto(0, 0)
p.write('Done')
time.sleep(3)
