import turtle as t
import random

tim = t.Turtle()

# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
t.colormode(255)

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  return tim.pencolor(r, g, b)

direction = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")
for x in range(200):
  # tim.color(random.choice(colours))
  random_color()
  tim.forward(30)
  tim.setheading(random.choice(direction))

screen = t.Screen()
screen.exitonclick()