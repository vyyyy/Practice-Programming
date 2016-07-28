import turtle

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    for i in range(4):
        brad.forward(100)
        brad.right(90)

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

def draw_triangle():
    triangleTurtle = turtle.Turtle()
    triangleTurtle.color("red")
    triangleTurtle.degrees(270)
    for i in range(3):
        triangleTurtle.forward(100)
        triangleTurtle.right(90)
        
def main():
    window = turtle.Screen()
    window.bgcolor("black")

    draw_square()

    draw_circle()

    draw_triangle()

    window.exitonclick()    

main()
