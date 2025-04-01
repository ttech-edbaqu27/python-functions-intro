# Task 1: Write a function addition() that prints the sum of 2 and 3.
def addition():
    print(2 + 3)

addition()
# Task 2: Prompt the user to enter two numbers.
# Then write a function that prints the product of those numbers.
# Bonus: handle invalid inputs.
num1 = input("Enter number 1: ")
num2 = input("Enter number 2: ")

def add():
    print(num1 * num2)

if num1.isnumeric() and num2.isnumeric():
    print(float(num1)*float(num2))


# Spiral Review: Given the following starter list, create a function that returns a list with only multiples of 3.
import random
starter = [random.randint(1, 10) for _ in range(10)]

# method 1: function
def filter3(lst):
    newList = []
    for element in lst:
        if element % 3 == 0:
            newList.append(element)
    return newList

def filter3a(lst):
    return [element for element in lst if element % 3 == 0] # list comprehension

print(filter3(starter))
print(filter3(starter))


# completed assignment