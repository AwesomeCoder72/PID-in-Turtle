import turtle
import time

bot = turtle.Turtle()
bot.showturtle()
bot.speed(9)

screen = turtle.Screen()
screen.setup(800, 400)

kP, kI, kD = 20, 0, 0
finished = False
error = 0

def drawLine(x):
  bot.pu()
  bot.goto(x, 100)
  bot.right(90)
  bot.pd()
  bot.forward(200)
  bot.pu()
  bot.goto(-100,0)
  bot.left(90)

def PID(x):
  drawLine(x)
  while not finished:
    position = bot.xcor()
    error = x - position
    print(error)
    movement = (error*kP)/12
    if error < 0:
      bot.backward(abs(movement))
    else:
      bot.forward(abs(movement))
    
    
    time.sleep(0.05)
  
PID(150)