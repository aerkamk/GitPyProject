import turtle
import random
import time
#DENEME12

def points(x, y):
    global point
    point = point +1
    write.clear()
    write.write('Poins {}'.format(point), align='center', font=('Courier', 24, 'normal'))
    arrow.goto(random.randint(-270, 270), random.randint(-270, 270))

window = turtle.Screen()
window.title('Reflex Game')
window.bgcolor('black')
window.setup(width=600, height=600)

arrow = turtle.Turtle()
arrow.speed(0)
arrow.shape('circle')
arrow.color('red')
arrow.penup()
arrow.goto(random.randint(-270, 270), random.randint(-270, 270))

point = 0

write = turtle.Turtle() 
write.speed(0) 
write.shape('square') 
write.color('white') 
write.penup() 
write.goto(0, 260) 
write.hideturtle() 
write.write('Click to Get Started:', align='center', font=('Courier', 24, 'normal'))

startTime = time.time()
timesecond = 30

second = turtle.Turtle() 
second.speed(0) 
second.shape('square') 
second.color('white') 
second.penup() 
second.goto(-250, -240) 
second.hideturtle() 
second.write('Second:{}'.format(int(time.time()-startTime)), align='center', font=('Courier', 12, 'normal'))


while True:
    while(time.time() - startTime) < timesecond:
        arrow.onclick(points)
        List = []
        
        if int(time.time()-startTime) != int(time.time()-startTime):
            second.clear()
            second.write('Seconds:{}'.format(int(time.time()-startTime)), align='center', font=('Courier', 12, 'normal'))
        else:
            second.clear()
        
    else:
        write.clear()
        write.write('Poins {}'.format(point), align='center', font=('Courier', 24, 'normal'))
        time.sleep(10)
        point = 0

print("Game is over!!!")