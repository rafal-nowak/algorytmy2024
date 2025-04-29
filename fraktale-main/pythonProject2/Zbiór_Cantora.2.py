from Zbiór_Cantora import fraktal_cantora
import time
from turtle import Turtle
zl = Turtle()

zl.penup()
zl.goto(-300,300)
zl.pendown()
zl.speed(0)

fraktal_cantora(zl, 300, 5)
time.sleep(10)