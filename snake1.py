import turtle
import time
import random

pospouse = 0.06

score = 0
high_score = 0

#window config
screen = turtle.Screen()
screen.title("Snake")
screen.bgcolor("black")
screen.setup(width = 600, height = 600)
screen.tracer(0)

#Snake head
serpiente = turtle.Turtle()
serpiente.speed(0)
serpiente.shape("square")
serpiente.shapesize(0.5, 0.5, 1)
serpiente.color("white")
serpiente.penup()
serpiente.goto(0, 0)
serpiente.direction = "stop"

#Foof
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

#Snake
snake = []

#Scores
text = turtle.Turtle()
text.speed(0)
text.color("white")
text.penup()
text.hideturtle()
text.goto(0, 269)
text.write("Score: {} 	High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))

#Functions
def top():
	if serpiente.direction != "down":
		serpiente.direction = "up"
def bottom():
	if serpiente.direction != "up":
		serpiente.direction = "down"
def left():
	if serpiente.direction != "right":
		serpiente.direction = "left"
def right():
	if serpiente.direction != "left":
		serpiente.direction = "right"

def mov():
	if serpiente.direction == "up":
		y = serpiente.ycor()
		serpiente.sety(y + 10)
	if serpiente.direction == "down":
		y = serpiente.ycor()
		serpiente.sety(y - 10)
	if serpiente.direction == "left":
		x = serpiente.xcor()
		serpiente.setx(x - 10)
	if serpiente.direction == "right":
		x = serpiente.xcor()
		serpiente.setx(x + 10)

def dead():
	global score
	time.sleep(1)
	serpiente.goto(0, 0)
	serpiente.direction = "stop"	
	for i in snake:
		i.clear()
		i.hideturtle()
	snake.clear()
	score = 0
	text.clear()
	text.write("Score: {} 	High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))


#Keys
screen.listen()
screen.onkeypress(top, "Up")
screen.onkeypress(bottom, "Down")
screen.onkeypress(left, "Left")
screen.onkeypress(right, "Right")

while True:
	screen.update()
	
	#colisiones border
	if serpiente.xcor() > 290 or serpiente.xcor() < -290 or serpiente.ycor() > 290 or serpiente.ycor() < -290:
		dead()
	
	if serpiente.distance(food) < 20:
		x = random.randint(-280, 280)
		y = random.randint(-280, 280)
		food.goto(x, y)

		cuerpo_serpiente = turtle.Turtle()
		cuerpo_serpiente.speed(0)
		cuerpo_serpiente.shape("square")
		cuerpo_serpiente.shapesize(0.5, 0.5, 1)
		cuerpo_serpiente.color("grey")
		cuerpo_serpiente.penup()
		snake.append(cuerpo_serpiente)

		score += 10

		if score > high_score:
			high_score = score

		if pospouse - 0.0005 > 0:
			pospouse = pospouse - 0.0005
			print(pospouse)
	



		text.clear()
		text.write("Score: {} 	High Score: {}".format(score, high_score), align = "center", font = ("Courier", 24, "normal"))

	#Move the snake body
	cuerpo_serpiente_total = len(snake)
	for i in range(cuerpo_serpiente_total - 1, 0, -1):
		x = snake[i - 1].xcor()
		y = snake[i - 1].ycor()
		snake[i].goto(x, y)

	if cuerpo_serpiente_total > 0:
		x = serpiente.xcor()
		y = serpiente.ycor()
		snake[0].goto(x, y)

	mov()

	for i in snake:
		if i.distance(serpiente) < 10:
			dead()


	
	time.sleep(pospouse)











screen.mainloop()