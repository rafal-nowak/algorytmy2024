from Płatek_kocha import platek_kocha
import time
from turtle import Turtle
zl = Turtle()

zl.penup()
zl.goto(-300,300)
zl.pendown()
zl.speed(0)

platek_kocha(zl, 3,200)
time.sleep(10)