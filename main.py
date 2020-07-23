import turtle

turtle.title("My Turtle Game")
turtle.bgcolor("black")
turtle.setup(600,600)

screen = turtle.Screen()
bob = turtle.Turtle()
bob.shape("turtle")
bob.color("white")
bob.speed(10)
bob.pensize(2)

def square(size):
  for i in range(4):
    bob.forward(size)
    bob.right(90)

def pattern():
  size = 50
  for i in range(108):
    square(size)
    bob.right(10)
    size -= 5


sally = turtle.Turtle()
sally.shape("turtle")
sally.color("blue")
sally.speed(20)
sally.pensize(2)

def spiral():
  steps = 5
  for i in range(500):
    sally.forward(steps)
    sally.left(91)
    steps += 1.5

#Alice.shape("turtle")
#Alice.color("blue")
#Alice.speed(5)
#Alice.pensize(2)

#def sphere(size):
#  shade = 75.0
#  alice.color(0.0,0.0,shade)
#  while size > 0:
#    alice.begin_fill()
#    alice.circle(size)
#    alice.end_fill()
#    size -= .5
#    shade += 1
#    alice.color((0,0,shade))

#sphere()
spiral()
pattern()