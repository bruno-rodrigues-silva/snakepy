import turtle


import time


import random


delay = 0.1
#first is set up the screen
wn = turtle.Screen()
#wn is the shortname for window
wn.title('Snake Game by Bruno Silva')
wn.bgcolor('dark blue')
wn.setup(width = 600, height = 600)
wn.tracer(0)

#Snake head
head =turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white')
head.penup()
head.goto(0, 0)
head.direction = 'stop'
#Snake food
food =turtle.Turtle()
food.speed(0)
food.shape('square')
food.color('green')
food.penup()
food.goto(0, 100)
segments = []
#Functions
def go_up():
    if head.direction != 'doown':
        head.direction = 'up'

def go_down():
     if head.direction != 'up':
        head.direction = 'down'

def go_right():
     if head.direction != 'left':
        head.direction = 'right'

def go_left():
     if head.direction != 'right':
         head.direction = 'left'


def move():
    if head.direction == 'up':
       y = head.ycor()
       head.sety(y + 20)
    elif head.direction == 'down':
       y = head.ycor()
       head.sety(y - 20)
    elif head.direction == 'right':
       head.setx(head.xcor() + 20)
    elif head.direction == 'left':
        head.setx(head.xcor() - 20)
#Keyboard bindings
wn.listen()
wn.onkeypress(go_up, 'Up' )
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_right, 'Right')
wn.onkeypress(go_left, 'Left')
# Main game loop
while True:
    wn.update()
    #Check for a collision with the boarder
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'
         #Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        #Clear the segments list
        segments.clear()

    #Check for a collision with the food
    if head.distance(food) < 20:
    # Move the food to a ramdom spot
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(random.randint(-290, 290), random.randint(-290, 290))
    
        food.goto(random.randint(-290, 290), random.randint(-290, 290))
        #Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape('square')
        new_segment.color('sky blue')
        new_segment.penup()
        segments.append(new_segment)
    #Move the end segments first in reverse order
    for index in range(len(segments) -1, 0, -1):
        x = segments[index -1].xcor()
        y = segments[index -1].ycor()
        segments[index].goto(x, y)

    #move segment 0 to were the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    #Check for head collisions with the body segments
    for segment in segments:
        if segment.distance(head)< 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = 'stop'
            #Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
            #Clear the segments list
            segments.clear()
    time.sleep(delay)
wn.mainloop()