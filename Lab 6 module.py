#Roberto J. Perez
#11/8/2022
#Lab 6
#CSS 225

#problem 1
import random as rand

for num in range(10):
    print(rand.randrange(25,36))
#problem 2
for i in range(0,100+1):
    if i%2==1:
        print(i)
#problem 3

days =("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

print(days)
input(print("Choose a day from the list\n",rand.choice(days)))
#problem 4
import math

print("Get the area of the circle")

r = float(input("Choose any number for your radius\n"))

area = math.pi * r**2

print("This is the area of your circle",area)
#problem 5
print("Find the answer too c")

a = float(input("pick any number for input a\n"))

b = float(input("pick any number for input b\n"))

c = math.sqrt(math.pow(a,2) + math.pow(b,2))

print("This is your answer for c",c)
#problem 6
num = int(input("Pick any number\n"))

n=1

for i in range(1,num+1):
    n = n * 1
print("Factorial of",num,"is",math.factorial(n))

