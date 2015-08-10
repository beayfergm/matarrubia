import turtle

def create_screen():
	window = turtle.Screen();
	window.bgcolor("red");
	return window;

def draw_square(turtle, size):
	turtle.shape("triangle");
	turtle.speed(10);
	turtle.color("white");

	for i in range(0, 4):
		turtle.forward(size);
		turtle.right(90);

	turtle.right(10);

def draw_circle(radius):
	angie = turtle.Turtle();
	angie.shape("turtle");
	angie.speed(3);
	angie.color("yellow");
	angie.circle(radius);

window = create_screen();

brad = turtle.Turtle();
for i in range(0, 36):
	draw_square(brad, 100);
# draw_circle(50);
window.exitonclick();


