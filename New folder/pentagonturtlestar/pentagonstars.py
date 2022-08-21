import turtle

tr = turtle.Turtle()
tr.speed(0)
tr.getscreen().bgcolor("black")
tr.color('lime')

def star (pop, size):
	if size <=10:
		return 
	else:
		for i in range(5):
			pop.forward(size)
			star(pop, size /2)
			pop.left(216)
		
star(tr, 200)

turtle.done()