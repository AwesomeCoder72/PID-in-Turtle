import turtle
import time

bot = turtle.Turtle()
bot.showturtle()
bot.speed(5)

screen = turtle.Screen()
screen.setup(800, 400)

kP = 0.7
kI = 0 
kD = 3
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
  previousError = 0
  while not finished:
    position = bot.xcor()
    error = x - position
    print(error)
    derivative = error - previousError

    movement = (error*kP + derivative*kD)
    bot.forward(movement)
    
    previousError = error
    time.sleep(0.05)
  
PID(150)