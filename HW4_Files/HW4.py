# HW4.py
# Author: Terrisha Edwards

### README
# This file contains buggy functions that you need to fix.
# There are 10 buggy functions in total.
# run test.py to see which functions are buggy and what the expected output is.
# remember you can run test.py with the -v flag to see more details about the tests.
# also remember that you can run a specific test by specifying the test name after the -k flag.
# you should not change the test.py file.

# Each function has a comment above it that describes what the function should do.
# Answer each question asking where the bug is in the buggy function.
# Provide your answer as what line the bug is on and what the bug is.
# For example, if the bug is on line 5 and the bug is that the function is missing a colon, you would write:
# 5: Missing colon
# After you fix the function, you should run test.py to make sure that the function is fixed.



def add(a:float, b:float) -> float:
    """Add two numbers together

    Args:
        a (float): number to add
        b (float): number to add

    Returns:
        float: the sum of a and b
    """
    return a + b
# Where is the bug in the buggy function?
# A: The bug is on line: return a - b. 
# Should be corrected to return a + b.  

def subtract(a:float, b:float) -> float:
    """Subtract two numbers

    Args:
        a (float): number to subtract from
        b (float): number to subtract

    Returns:
        float: the difference of a and b
    """
    return a - b
# Where is the bug in the buggy function?
# A: The bug is on line: return a + b. 
# Should be corrected and return a - b. 

def divide(a, b):
    """Divide two numbers

    Args:
        a (float): number to divide
        b (float): number to divide by

    Returns:
        float: the quotient of a and b
    """
    return a / b
# Where is the bug in the buggy function?
# A: The bug is on line: return a * b. 
# Should be changed to: return a / b. 


def multiply(a:float, b:float) -> float:
    """Multiply two numbers

    Args:
        a (float): number to multiply
        b (float): number to multiply by

    Returns:
        float: the product of a and b
    """
    return a * b

# Where is the bug in the buggy function?
# A: The bug is on line: return a / b. 
# Should be changed to return a * b. 


def greet(name:str)->str:
    """Greet a person

    Args:
        name (str): name of the person to greet

    Returns:
        _type_: the greeting message
    """
    return "Hello, "+ name +"!"
# Where is the bug in the buggy function?
# A: The bug is on line: return "Heloo, "+name+"!". 
# There is a typo in the string and it should be changed to: return "Hello, "+ name +"!". 


def square(num:int) -> int:
    """Square a number

    Args:
        num (int): number to square

    Returns:
        int: the square of the number
    """
    return num * num
# Where is the bug in the buggy function?
# A: The bug is in on the line "return num + num". 
# Should be changed to: return num * num


def is_even(num:int) -> bool:
    """Check if a number is even

    Args:
        num (int): number to check

    Returns:
        bool: True if the number is even, False otherwise
    """
    return num % 2 == 0
# Where is the bug in the buggy function?
# A: The bug is on line 7: return num % 2 == 1. 
# Should be changed to return num % 2 == 0


def grade_calculator(score:float) -> str:
    """Calculate the grade based on the score

    Args:
        score (float): score to calculate the grade for

    Returns:
        str: the grade for the score
    """
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score < 90:
        return "B"
    elif 70 <= score < 80:
        return "C"
    elif 60 <= score < 70:
        return "D"
    elif 0 <= score < 60:
        return "F"
    else:
        return "Invalid Score"
# Where is the bug in the buggy function?
# A: The bug is on the line: elif 70 <= score < 79. 
# Should be corrected to elif 70 <= score < 80. 

def speed_check(speed:float) -> str:
    """Check if the speed is within the speed limit
    
    Args:
        speed (float): speed to check
        
    Returns:
        str: the speed check result
    """
    # Assuming general speed limits: min: 20, max: 70 (in mph)
    if speed < 20:  
        return "Too slow"
    elif 20 <= speed <= 60:
        return "Within limit"
    elif speed > 60: 
        return "Over speed limit"
    else:
        return "Unknown"
# Where is the bug in the buggy function?
# A: The bug is on the line: elif speed > 70: return "Over speed limit". 
# Should be corrected to elif speed > 60: return: "Over the speed limit".

def is_leap_year(year:int) -> bool:
    """Check if a year is a leap year

    Args:
        year (int): year to check

    Returns:
        bool: True if the year is a leap year, False otherwise
    """
    if year % 4 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 400 == 0:
        return True
    else:
        return False
# Where is the bug in the buggy function?
# A: The bug is the calculations are that within the leap year.
#  If a year is divisible by 4, it's a leap year but if it's divisible by 100, it's not a leap year unless it's also divisible by 400, in which it is a leap year.







def main():
    print("You are running me directly!")

if __name__ == "__main__":
    main()
