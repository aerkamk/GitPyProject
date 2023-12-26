import turtle
import time
import random
#Test12345


speed =(0.05) 
window = turtle.Screen()
window.title('Snake Game')
window.bgcolor('black')
window.setup(width=600, height=600)
window.tracer(0)

snakeHead = turtle.Turtle()
snakeHead.speed(0)
snakeHead.shape('circle')
snakeHead.color('white')
snakeHead.penup()
snakeHead.goto(0, 100)
snakeHead.direction = 'stop'

food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('green')
food.penup()
food.goto(0, 0)
food.shapesize(0.90, 0.90)
shapeList = ('circle','square','triangle','turtle','classic') 
tails = []
points = 0

write = turtle.Turtle()
write.speed(0)
write.shape('circle')
write.color('white')
write.penup()
write.goto(0, 260)
write.hideturtle()
write.write('Points: {}'.format(points), align='center', font=('Courier', 24, 'normal'))

developer = "AEK"
cprt = turtle.Turtle()
cprt.speed(0)
cprt.shape('circle')
cprt.color('white')
cprt.penup()
cprt.goto(-280, -280)
cprt.hideturtle()
cprt.write('Developer: {}'.format(developer), align='left', font=('Courier', 12, 'normal'))

def move():
    if snakeHead.direction == 'up':
        y = snakeHead.ycor()
        snakeHead.sety(y+10)

    if snakeHead.direction == 'down':
        y = snakeHead.ycor()
        snakeHead.sety(y-10)

    if snakeHead.direction == 'right':
        x = snakeHead.xcor()
        snakeHead.setx(x+10)

    if snakeHead.direction == 'left':
        x = snakeHead.xcor()
        snakeHead.setx(x-10)

def goUP():
    if snakeHead.direction != 'down':
        snakeHead.direction = 'up'
    
def goDown():
    if snakeHead.direction != 'up':
        snakeHead.direction = 'down'

def goRight():
    if snakeHead.direction != 'left':
        snakeHead.direction = 'right' 

def goLeft():
    if snakeHead.direction != 'right':
        snakeHead.direction = 'left' 

window.listen()
window.onkey(goUP,'Up')
window.onkey(goDown,'Down')
window.onkey(goRight,'Right')
window.onkey(goLeft,'Left')

## Hello Word!
time.sleep(1)


while True:
    window.update()

    if snakeHead.xcor() > 300 or snakeHead.xcor() < -300 or snakeHead.ycor() > 300 or snakeHead.ycor() < -300:
        time.sleep(1)
        snakeHead.goto(0, 0)
        snakeHead.direction = 'stop'
        for tail in tails:
            tail.goto(1000, 1000)
        
        tails = []
        write.clear()
        points = 0
        write.write('Points: {}'.format(points), align='center', font=('Courier', 24, 'normal'))
        speed = 0.05


    if snakeHead.distance(food) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)

        food.shape(random.choice(shapeList))
        food.goto(x, y)

        points = points + 10
        write.clear()
        write.write('Points: {}'.format(points), align='center', font=('Courier', 24, 'normal'))

        speed = speed - 0.001

        newTail = turtle.Turtle()
        newTail.speed(0)
        newTail.shape('square')
        newTail.color('white')
        newTail.penup()
        tails.append(newTail)


    for i in range(len(tails) - 1, 0, -1):
        x = tails[i - 1].xcor()
        y = tails[i - 1].ycor()
        tails[i].goto(x, y)
    
    if len(tails) > 0:
        x = snakeHead.xcor()
        y = snakeHead.ycor()
        tails[0].goto(x, y)
    
    move()
    time.sleep(speed)