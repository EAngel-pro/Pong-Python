import turtle
import winsound
#winsound.PlaySound("x.y", winsound.SND_ASYNC)
#main
root = turtle.Screen()
root.title("Pong")
root.bgcolor("black")
root.setup(width=800, height=600)
root.tracer(0)
speed1 = 0.2
#Score
def writescore():
	pen.clear()
	pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))
scoreA = 0
scoreB = 0
#A
Pad_A = turtle.Turtle()
Pad_A.speed(0)
Pad_A.shape("square")
Pad_A.color("white")
Pad_A.shapesize(stretch_wid=5, stretch_len=1)
Pad_A.penup()
Pad_A.goto(-350, 0)
#B
Pad_B = turtle.Turtle()
Pad_B.speed(0)
Pad_B.shape("square")
Pad_B.color("white")
Pad_B.shapesize(stretch_wid=5, stretch_len=1)
Pad_B.penup()
Pad_B.goto(350, 0)
#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = speed1
ball.dy = speed1
#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
writescore()
winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
#Functions
def padAup():
	y = Pad_A.ycor()
	y += 20
	Pad_A.sety(y)
def padAdown():
	y = Pad_A.ycor()
	y -= 20
	Pad_A.sety(y)
def padBup():
	y = Pad_B.ycor()
	y += 20
	Pad_B.sety(y)
def padBdown():
	y = Pad_B.ycor()
	y -= 20
	Pad_B.sety(y)
#Keybindings
root.listen()
root.onkeypress(padAup, "w")
root.onkeypress(padAdown, "s")
root.onkeypress(padBup, "Up")
root.onkeypress(padBdown, "Down")
#end
while True:
	root.update()
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)
	if ball.ycor() > 290:
		ball.sety(290)
		ball.dy *= -1
	if ball.ycor() < - 290:
		ball.sety(-290)
		ball.dy *= -1
	if ball.xcor() > 390:
		ball.goto(0, 0)
		ball.dx *= -1
		scoreA += 1
		writescore()
	if ball.xcor() < -390:
		ball.goto(0, 0)
		ball.dx *= -1
		scoreB += 1
		writescore()
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < Pad_B.ycor() + 40 and ball.ycor() > Pad_B.ycor() - 40):
		ball.setx(340)
		ball.dx *= -1
	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < Pad_A.ycor() + 40 and ball.ycor() > Pad_A.ycor() - 40):
		ball.setx(-340)
		ball.dx *= -1
	#loopend
