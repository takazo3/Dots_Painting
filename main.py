import turtle as t
import random
screen = t.Screen()

tim = t.Turtle()
tim.speed("fastest")

t.colormode = (255)



color_list = [(202, 164, 109), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


tim.seth(225)
tim.pu()
tim.forward(300)
tim.seth(0)
number_of_dots = 100
tim.hideturtle()


for dot_count in range(1, number_of_dots + 1):
    screen.colormode(255)
    tim.color(random.choice(color_list))
    tim.pd()
    tim.dot(20)
    tim.pu()
    tim.fd(50)
    if dot_count % 10 == 0:
        tim.seth(90)
        tim.fd(50)
        tim.seth(180)
        tim.fd(500)
        tim.seth(0)


screen.exitonclick()