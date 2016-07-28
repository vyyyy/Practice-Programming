import turtle

def draw_square(some_square):
    for i in range(36):
        for i in range(4):
            some_square.forward(100)
            some_square.right(90)
        some_square.right(10)

def main():
       #instantiate the canvas
       window = turtle.Screen()
       window.bgcolor("red")
       #instantiate the turtle
       mySquare = turtle.Turtle()
       mySquare.shape("turtle")
       mySquare.color("yellow")
       mySquare.speed("fast")
       #call the drawing function
       draw_square(mySquare)
       #close the window
       window.exitonclick()

main()
    
