from Drzewo_binarne import drzewo_binarne
import time
from turtle import Turtle
zl = Turtle()

zl.penup()
zl.goto(-20,-20)
zl.pendown()
zl.left(90)
zl.speed(0)

drzewo_binarne(zl, 3, 50)
time.sleep(10)
