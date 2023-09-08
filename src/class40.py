import turtle

while True:
    for i in range(100):
        turtle.forward(300)
        turtle.left(100)
    print(turtle.position())
    break

turtle.done()
