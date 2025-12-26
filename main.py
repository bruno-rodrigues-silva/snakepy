import turtle
#first is set up the screen
wn = turtle.Screen()
#wn is the shortname for window
wn.title('Snake Game by Bruno Silva')
wn.bgcolor('green')
wn.setup(width = 600, height = 600)
wn.tracer(0)

#Snake head
head =turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('blue')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

#Functions
def move():
   if head.direction == 'up':
       y = head.ycor()
       head.sety(y + 20)
# Main game loop

while True:
    wn.update()
wn.mainloop()


