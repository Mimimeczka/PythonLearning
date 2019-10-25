# '''slupek z szesciokątów'''
# import turtle
# zolw = turtle.Turtle()
# colors = ["yellow", "black", "brown", "green", "white", "pink", "purple", "gray", "blue"]
# zolw.color("red", "red")
# for c in range(9):
#     zolw.begin_fill()
#     for i in range(6):
#         zolw.forward(100 - 10 * c)
#         zolw.right(60)
#     zolw.end_fill()
#     zolw.color("red", colors[c])
#     zolw.pencolor(colors[c - 1])
#     zolw.goto(zolw.position()[0] + 5, zolw.position()[1] - 8)
#     zolw.pencolor("red")
# turtle.done()
#
# '''szesciokąt'''
# import turtle
# zolw = turtle.Turtle()
# zolw.color("red", "blue")
# zolw.begin_fill()
# for i in range(6):
#     zolw.forward(100)
#     zolw.right(60)
# zolw.end_fill()
# turtle.done()
#
# '''sloneczko'''
# import turtle
# zolw = turtle.Turtle()
# zolw.pencolor("orange")
# zolw.speed(150)
# for i in range(60):
#     zolw.forward(150)
#     zolw.right(5)
#     zolw.forward(150)
#     zolw.left(4)
#     zolw.forward(100)
#     zolw.penup()
#     zolw.goto(0, 0)
#     zolw.pendown()
#     zolw.right(5)
# turtle.done()
#
# '''sloneczko'''
# import turtle
# zolw = turtle.Turtle()
# zolw.color("red", "yellow")
# zolw.speed(5)
# zolw.begin_fill()
# while True:
#     zolw.forward(200)
#     zolw.left(170)
#     if abs(zolw.pos()) < 1:
#         break
# zolw.end_fill()
# turtle.done()
#
# '''rysowanie kropek'''
# import turtle
# zolw = turtle.Turtle()
# zolw.penup()
# for i in range(10):
#     for j in range(5):
#         zolw.dot()
#         zolw.forward(10)
#     zolw.backward(5 *10)
#     zolw.goto(zolw.pos()[0], zolw.pos()[1] - 10)
# turtle.done()
#
# '''stemple'''
# import turtle
# zolw = turtle.Turtle()
# window = turtle.Screen()
# window.bgcolor("red")
# zolw.shape("turtle")
# zolw.color("white")
# size = 10
# zolw.penup()
# zolw.speed(10)
# for i in range(100):
#     zolw.stamp()
#     size += 3
#     zolw.forward(size)
#     zolw.right(300)
# turtle.done()


