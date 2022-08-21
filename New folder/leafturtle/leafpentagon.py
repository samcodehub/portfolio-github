import turtle

bill = turtle.Turtle()
bill.speed(0)
bill.shape('turtle')
bill.color('lime')
window = turtle.Screen()
window.bgcolor("black")
bill.pensize(2)
bill.penup()
bill.left(90)
bill.forward(60)
bill.left(90)
bill.forward(60)
bill.left(180)
bill.pendown()
def draw(t,n):
	if n < 10:
		t.forward(n)
		return
	m = n/3
	angle = 60
	draw(t,m)
	t.left(angle)
	draw(t,m)
	t.right(2*angle)
	draw(t,m)
	t.left(angle)
	draw(t,m)
def snowflake(t,n):
	for i in range(3):
		draw(t,n)
		t.right(120)
bill.fillcolor('forestgreen')
bill.begin_fill()
snowflake(bill,300)
bill.end_fill()
bill.hideturtle()
turtle.mainloop()
