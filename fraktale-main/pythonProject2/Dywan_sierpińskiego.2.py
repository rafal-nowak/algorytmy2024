from Dywan_sierpińskiego import dywan_sierpinskiego
import time
from turtle import Turtle
zl = Turtle()

zl.penup()
zl.goto(-300,300)
zl.pendown()
zl.speed(0)

dywan_sierpinskiego(zl, 3, 500)
time.sleep(10)