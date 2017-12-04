#!usr/bin/python
from turtle import Turtle
import time


p = Turtle()
p.pensize(5)
p.up()
p.goto(-50, 0)
p.down()
p.speed(3)

for i in range(6):
    p.forward(100)
    p.right(144)
time.sleep(3)
