# HW5.py
# Author: Terrisha Edwards 

# This homework assignment tests on list in python

# Question 1: Create a list with 5 of your favorite foods. Print the list
favorite_foods = ("Jerk_Chicken", "Curry_Chicken", "Oxtail", "Baked Mac_Cheese", "Pizza")
print(favorite_foods)
# Question 2: Using the list from question 1, print the first and last element of the list
print("First favorite food:", favorite_foods[0])
print("Last favorite food:", favorite_foods[-1])

# Question 3: Using the list from question 1, print the 3rd element of the list
print("Third favorite food:", favorite_foods[2])

# Question 4: Using the list from question 1, print the 1st through 3rd elements of the list using list slicing
print("First three davorite food:", favorite_foods[:3])

# Question 5: Using the list from question 1, print the last 2 elements of the list using list slicing
print("Last two favorite food:", favorite_foods[-2])

# Question 6: Using the list from question 1, create a for each loop that prints each element of the list
for food in favorite_foods:
    print(food)
# Question 7: Using the list from question 1, create a for loop that prints each element of the list in reverse order
for food in reversed(favorite_foods):
    print(food)
# Question 8: Using the list from question 1, create a for loop that prints each element of the list and its index (hint use the enumerate() function)
for index, food in enumerate(favorite_foods):
    print(f"Food at index{index}: {food}")

# Question 9: Using this list of lists, print the first element of the second list (hint: use indexing)
list = [[1,2,3],[4,5,6],[7,8,9]]
print("First element of the second list:", list[1][0])
# Question 10: Create a function that will take in a list and return the list in reverse order
# Hint: You can take in a list as a parameter and return a list
def reverse_list(input_list):
    return input_list[::-1]

