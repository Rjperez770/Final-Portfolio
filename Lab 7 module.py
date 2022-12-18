#Roberto J. Perez
#11/20/2022
#Lab 7
#CSS 225

#problem 1
import math

def areaOfCircle(r):
    area = math.pi * r **2
    return area
areaOfCircle(3)
#problem 2
def test_range(n):
    if n in range(1,11):
        print("True")
    else:
        print("False")
test_range(1)
#problem 3
def list_multiply(n):
    total = 1
    for n in n:
        total = total * n
    return total
list = [7,10,7,9]
print(list_multiply(list))
#problem 4
my_list = [1, 3, 3, 3, 6, 2, 3, 5]

def list_check(a_list):
    newlist = []
    for e in a_list:
        if e not in newlist:
            newlist.append(e)
    return newlist

print(list_check(my_list))
#problem 5
import turtle

def drawSquare(t, sz):
    for i in range(4):
        t.forward(sz)
        t.left(90)
wn = turtle.Screen()

alex = turtle.Turtle()
alex.color("blue")

wn.exitonclick()




