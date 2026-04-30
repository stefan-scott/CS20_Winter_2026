import turtle
import random

window = turtle.Screen()
window.bgcolor('lightblue')
window.setup(600,600)

#create the turtles, and specify their attributes
lance = turtle.Turtle()
andy = turtle.Turtle()
lance.color('red')
andy.color('blue')
lance.shape('turtle')
andy.shape('turtle')

# move the turtles to their starting locations
andy.penup()
lance.penup()
andy.goto(-250,20)
lance.goto(-250,-20)

# race 3 (modified):
#for i in range(150):
while andy.xcor() < 250 and lance.xcor() < 250:
    andy.fd(random.randrange(1,5))
    lance.fd(random.randrange(1,5))
    print(f"{andy.xcor()}  {lance.xcor()}")

if andy.xcor() > lance.xcor():
    print("ANDY WINS!")
elif andy.xcor() < lance.xcor():
    print("LANCE WINS!")
else:
    print("race ended in a tie...")
# race 2:
# for i in range(random.randrange(10,101)):
#     andy.fd(5)
#     
# for i in range(random.randrange(10,101)):
#     lance.fd(5)
    

# race 1: single random move for each turtle
# easy to code, no concurrency, different dist
# andy.fd(random.randrange(300,500))
# lance.fd(random.randrange(300,500))

window.exitonclick()
