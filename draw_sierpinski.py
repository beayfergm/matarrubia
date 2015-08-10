import turtle

colormap = ['red','orange','yellow','green','blue',
            'brown','black']
speed = 100

def drawTriangle(turtle, points,color):
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(points[0][0],points[0][1])
    turtle.down()
    turtle.begin_fill()
    turtle.goto(points[1][0],points[1][1])
    turtle.goto(points[2][0],points[2][1])
    turtle.goto(points[0][0],points[0][1])
    turtle.end_fill()

def getMiddlePoint(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(turtle, points, degree):

    drawTriangle(turtle, points,colormap[degree])
    if degree > 0:
        sierpinski(turtle, [points[0],
		                    getMiddlePoint(points[0], points[1]),
		                    getMiddlePoint(points[0], points[2])],
		               		degree-1)
        sierpinski(turtle, [points[1],
	                        getMiddlePoint(points[0], points[1]),
	                        getMiddlePoint(points[1], points[2])],
	                   		degree-1)
        sierpinski(turtle, [points[2],
	                        getMiddlePoint(points[2], points[1]),
	                        getMiddlePoint(points[0], points[2])],
	                   		degree-1)

def main():
   turtle_instance = turtle.Turtle()
   turtle_instance.speed(speed)
   window = turtle.Screen()
   reference_points = [[-100,-50],[0,100],[100,-50]]
   sierpinski(turtle_instance, reference_points,5)
   window.exitonclick()

main()