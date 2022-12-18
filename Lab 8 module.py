#Roberto J. Perez
#12/1/2022
#CSS 225
#Module 8

#Problem 1
def equal(num1, num2):
    if num1 == num2:
        print("equal")
    else:
        print("sorry not equal")

num1 = input("insert any number from 1-10\n")

num2 = input("insert any number from 1-10\n")

print(equal(num1,num2))
#Problem 2
def sum(x, y):
    sum = int()
    if sum < 10:
        print("sum is less than 10")
    elif sum > 10:
        print("sum is greater than 10")
    else:
        print("sum is equal to 10")

x = int(input("Pick any number to add\n"))

y = int(input("Pick another number to add\n"))

print(sum(x, y))
#problem 3
list1 = [1,4,5,5,2,3]

def list(a_list):
    newlist = []
    if 5 in newlist:
         print(newlist)

    for a in a_list:
        if a not in newlist:
            newlist.append(a)
    return newlist

print(list(list1))
#problem 4
def y_leap(year):
    leap = False
    if year % 4 ==0:
        leap = True
    elif year % 100 ==0:
        leap = False
    elif year % 400 ==0:
        leap = True
    return leap
year = int(input("Enter year to check if it is leap year.\n"))

print(y_leap(year))
#problem 5.1
class character:
 def __init__(self, nickname, weapons, weaknesses):
    self.nickname = nickname
    self.weapons = weapons
    self.weaknesses = weaknesses
def get_model(self):
    return self.nickname
def get_year(self):
    return self.weapons
def get_color(self):
    return self. weaknesses
def profile(self):
    return self.nickname, self.weapons, self. weaknesses
player1 = character('','','')
player1.nickname = 'Mount. Climber'
player1.weapons = ['coat', 'first aid kit', 'rope']
player1.weaknesses = ['fast']
for item in player1.weapons:
    print("Item: ", item)
for debuff in player1.weaknesses:
    print("Debuff: ", debuff)
#problem 5.2
player1 = character('','','')
player1.nickname = 'Mount. Climber'
player1.weapons = ['pan', 'groceries']
player1.weaknesses = ['big']
for item in player1.weapons:
    print("Item: ", item)
for debuff in player1.weaknesses:
    print("Debuff: ", debuff)
#problem 5.3
player1 = character('','','')
player1.nickname = 'Mount. Climber'
player1.weapons = ['pen', 'idea', 'paper']
player1.weaknesses = ['focused']
for item in player1.weapons:
    print("Item: ", item)
for debuff in player1.weaknesses:
    print("Debuff: ", debuff)

