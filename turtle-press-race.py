# don't run in linux and macos because i haven't tested and there might be a lot of bugs
import turtle
import time

draw = turtle.Turtle()
window = turtle.Screen()
help = turtle.Turtle()
window.title("Turtle Press Race!")
redscore = 0
bluescore = 0
window.setup(width=1200, height=700)



pen = turtle.Turtle()
pen.pensize(3)
pen.penup()
pen.goto(0, 250)
pen.pendown()
pen.write("Turtle Press Race!", align="center", font=("Monospace", 48, "bold"))
pen.hideturtle()

# score = turtle.Turtle()
# score.penup()
# score.goto(400, 220)
# score.hideturtle()
# score.write("Red: 0 | Blue: 0", align="center", font=("Monospace", 13))

pen2 = turtle.Turtle()
pen2.pensize(3)
pen2.penup()
pen2.goto(0, -130)
pen2.pendown()
pen2.hideturtle()

end = turtle.Turtle()
end.pensize(3)
end.penup()
end.goto(0, -200)
end.pendown()
end.hideturtle()

start = turtle.Turtle()
start.pensize(3)
start.penup()
start.goto(0, 80)
start.pendown()
start.hideturtle()

def racetrack():

    draw.speed(6)
    x = -500
    y = 200

    for linesx in range(3):
        draw.penup()
        draw.goto(x, y)
        y -= 100
        draw.pendown()
        draw.forward(1000)
        draw.penup()

    y = 200
    draw.right(90)
    for linesy in range(2):
        draw.penup()
        draw.goto(x, y)
        x += 1000
        draw.pendown()
        draw.forward(200)
        draw.penup()

    y = 200
    x = -350
    draw.goto(x, y)
    draw.pendown()
    for linedown in range(25):
        draw.forward(5)
        draw.penup()
        draw.forward(3)
        draw.pendown()
    draw.hideturtle()

    food1 = turtle.Turtle()
    food1.shape('square')
    food1.penup()
    food1.goto(510, 150)
    food1.write("      food1", font=("Monospace", 8))

    food2 = turtle.Turtle()
    food2.shape('square')
    food2.penup()
    food2.goto(510, 50)
    food2.write("      food2", font=("Monospace", 8))

player1 = turtle.Turtle()
player2 = turtle.Turtle()

def playagain():
    start.clear()
    draw.left(270)
    end.clear()
    window.onkey(fun=None, key='s')
    window.onkey(fun=None, key='l')
    window.onkey(fun=None, key='S')
    window.onkey(fun=None, key='L')
    window.onkey(fun=None, key='space')
    pen2.clear()
    player1.clear()
    player2.clear()
    racer()

def racer():
    end.write("quackk.....~~", align="center", font=("Monospace", 20))
    player1.color("red")
    player2.color("blue")

    player1.shapesize(stretch_wid=2)
    player2.shapesize(stretch_wid=2)

    player1.penup()
    player2.penup()

    player1.shape('turtle')
    player2.shape('turtle')
    player1.goto(-420, 150)
    player2.goto(-420, 50)
    start.clear()
    start.write("Ready...", align="center", font=("Monospace", 20))
    time.sleep(3)
    start.clear()
    start.write("GO!", align="center", font=("Monospace", 20))
    window.listen()
    window.onkey(fun=goone, key='s')
    window.onkey(fun=gotwo, key='l')
    window.onkey(fun=goone, key='S')
    window.onkey(fun=gotwo, key='L')
    window.onkey(fun=None, key='space')
    end.clear()
    input()
def goone():
    player1.forward(15)
    player2.backward(5)
    if player1.xcor() > 490:
        # redscore += 1
        pen2.color('red')
        pen2.write("Red won!", align="center", font=("Monospace", 48, "bold"))
        player1.write("           :>\n\n", font=("Monospace", 8, "bold"))
        player2.write("           :[ \n\n", font=("Monospace", 8, "bold"))
        window.onkey(fun=None, key='s')
        window.onkey(fun=None, key='l')
        window.onkey(fun=None, key='S')
        window.onkey(fun=None, key='L')
        player1.left(360)
        end.color('black')
        end.write("Press Space To Play Again...", align="center", font=("Monospace", 20))
        window.listen()
        window.onkey(fun=playagain, key='space')
def gotwo():
    player2.forward(15)
    player1.backward(5)
    if player2.xcor() > 490:
        # bluescore += 1
        pen2.color('blue')
        pen2.write("Blue won!", align="center", font=("Monospace", 48, "bold"))
        player2.write("           :] \n\n", font=("Monospace", 8, "bold"))
        player1.write("           :<\n\n", font=("Monospace", 8, "bold"))
        window.onkey(fun=None, key='s')
        window.onkey(fun=None, key='l')
        window.onkey(fun=None, key='S')
        window.onkey(fun=None, key='L')
        player2.left(360)
        end.color('black')
        end.write("Press Space To Play Again...", align="center", font=("Monospace", 20))
        window.listen()
        window.onkey(fun=playagain, key='space')

help.penup()
help.shape("turtle")
help.goto(0, -50)
help.write("           red press S\n           blue press L\n           this is my first graphic game created by me so support me at damduchuy.github.io")
help.left(90)

racetrack()
racer()
