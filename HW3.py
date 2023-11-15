# HW3.py
# Author: Terrisha Edwards

# This Homework assignment is meant to test your ability to make functions within python as well as importing and using modules. This assignment might require you to do some research on your own. If you get stuck, try googling the problem, especially when it comes to importing and using the different modules.

# Question 1:
# Write a function that takes in a number and returns that number squared
# IE. If the user inputs 3, the function should return 9
def square_number(number)
    return number **2
result = square_number(3)
print(result)
# Question 2:
# Write a function that takes in a string, a letter, and a number and returns the string with the letter replaced at the number index
# IE. If the user inputs "Hello World", "a", and 3, the function should return "Helao World"

# Question 3:
# Write a function that takes in a number, a lower bound, and an upper bound and returns whether the number is within the bounds
# IE. If the user inputs 5, 1, and 10, the function should return True
number = 5
lower_bond = 1
upper_bound = 10


# Question 4:
# Write a function that asks the user for their name, age, and favorite color. Then write a function that accepts those three parameters and prints them out in a sentence
# IE. If the user inputs "John", 20, and "blue", the function should print "Hello, my name is John. I am 20 years old. My favorite color is blue."
# Hints: You will need to use the input() function to get the user's input. You will also need to use the str() function to convert the age to a string
# This is a two part question. You will need to write two functions
# remember in class we learned you can return miltiple values from a function
# also remember in class you can pass in pultiple variables into a function

def get_user_info():
    name = input("Enter your name")
    age = int(input("Enter your age"))
    color = input("Enter your favorite color: ")


def print_user_info(name, age, color):
    print("Hello my name is John")
    print("I am " + 20 +" years old")
    print("My favorite color" is "+ blue +")

# Question 5:
# import the random module and use it to generate a random number between 1 and 100
random_number = "random.randint(1,100)"

# Question 6:
# import the math module and use it to find the square root of 16 (hint: use the sqrt() function)
import math

sqare_root = math.sqrt(16)


# Question 7:
# import the sys module and use it to display the version of python you are using
# this time import the module using the import "as" keyword
# hint: use the version attribute (sys.version)
import sys as system

python_version = system.version
print("python version:", python_version)

# Question 8:
# import the os module and use it to display the current working directory. This time import the module using the from keyword
# hint: use the getcwd() function

from os import getcwd
#Display the current working directory
current_directory = getcwd()
print("Current working directory")