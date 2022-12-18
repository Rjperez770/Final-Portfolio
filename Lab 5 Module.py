#Roberto J. Perez
#11/3/2022
#CSS 225
#Lab 5
#Problem 1
Hello = "Hello World!\n"
print(100 * Hello)
#problem 2
num_list = [12, 10, 32, 3, 66, 17, 42, 99, 20]
for i in num_list:
    print(i)

for i in num_list:
    print("The square of",i,"is",i**2)
#Problem 3
import turtle as t

tom = t.Turtle()

l = print(int(input("Enter your length of the side on the shape\n")))
color = print(str(input("pick a color to fill in the shape\n")))
shape = print(str(input("pick from a triangle or square\n ")))


if shape == "triangle":
    for num in range(3):
        tom.begin_fill()
        tom.forward(l)
        tom.filling(color)
        tom.right(120)
        tom.end_fill()
elif shape == "square":
    for num in range(4):
        tom.begin_fill()
        tom.forward(l)
        tom.filling(color)
        tom.right(90)
        tom.end_fill()

input()
#Problem 4
for num in range(1,51):
    print(num)
    if num % 3 == 0:
        print("Divisible by 3")
    elif num % 5 == 0:
        print("Divisible by 5")
    else:
        print("Divisible by both")




