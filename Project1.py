# Project1.py
# Author: Terrisha Edwards 


# This project is meant to test your ability from everything we have learned so far in class
# You will need to use variables, if statements, loops, and functions

# Quiz Game:
# Create a simple console-based quiz game where the user answers a series of questions.
# The game should keep track of the user's score and provide feedback based on the answers given.

# Write a function that displays a welcome message to the user and explains the rules of the game
def welcome_message(): 
    print("Hello welcome to Lucky 68!")
    print("Rules of the Game:")
    print("For this quest you have to achieve a total score of 68.")
    print("You will start with a score of 0, and you will have to accumlate points to achieve the Lucky 68.")
    print("You can earn points by completing various tasks or challenges.")
    print("Each task will have a differemt point value.")
    print("The game will continue until you reach a score of 68")
    print("Good Luck and Have Fun!")

# Implement at least 5 , each with 4 questions answer options (a, b, c, d). Each question should be worth 1 point.
def ask_question(question, options, correct_answer):
    print(question)
    for option in options:
        print(option)
        user_answer = input("Your answer (a, b, c, d):")
        return user_answer == correct_answer
    
def display_result(is_correct):
    if is_correct:
        print("Correct! You earned points.")
        return 1
    else:
        print("Incorrect. The correct answer was provided.")
        return 0 
def display_final_score(scoer):
    print("Congrats! Your final score is: 68")
    
#Question

questions = [

    {
        'questions': "What is the capital of New Jersey?"
        'options':['a: Trenton', 'b:Seaside Heights', 'c:Priceton', 'd:Newark']
        'correct_answer': 'a'
    },
    {
        'question': "Which nickname is often used to refer to New Jersey?"
        'options':['a:The Empire State','b:The Sunshine','c:The Garden State','d:The Lone Star State']
        'correct_answer':'c'
    }
    {
        'questions': "How many lakes does Stockton University Have?"
        'options':['a:4', 'b:6', 'c:8', 'd:2']
        'correct_answer':'d'
    },
    {
        'questions': "Who is the governor of New Jersey?"
        'options':['a:Jon Corzine', 'b:Phil Murphy', 'c:Richard Codey', 'd:Chris Christie']
        'correct_answer':'b'
    {
        'questions': "How man counties are in NEw Jersey?"
        'options':['a:35', 'b:52', 'c:21', 'd:44']
        'correct_answer':'c'
    }   

    }

]

def main():
        welcome_message()
        total_score = 0
        target_score = 68
        
for q in questions: 
    is_correct = ask_question(q['question']), q['options'], q['correct_answer'])
    
    
if total_score >= target_score >= target_score:
    break

display_final_score(toal_score)


# For each question, display the question and the answer options to the user.
# Use input() to get the user's answer.
# 1. Ask the user for the capital of New Jersey and assign it to a variable called "capital".
capital = input ("What is the capital of New Jersey?")
print("capital")

# 2. Ask the user which nickname is often used to refer to New Jersey and assign it to a variable called "nickname".
nickname = int(input("Which nickname is often used to refer to New Jersey"))
print("nickname")

# 3. Ask the user How many lakes does Stockton University have and assign it to a variable called "lakes".
lakes = int(input("How many lakes does Stockton University have?"))
print("lakes")

# 4. Ask the user Who is the governor of New Jersey and it to the variable called "governor".
governor = int(input("Who is the governor of New Jersey?"))
print("governor")

# 5. Ask the user How many counties are in New Jersey and assign it to the variable called "counties".
counties = int(input("How many counties are in New Jersey?"))
print("counties")

# Use if or if-else statements to check if the answer is correct.
input_number = int(input("correct answer: "))
if input_number < 68:
    print("negative")
elif input_number > 68:
    print("positive")
else:
    print("zero")

user_answer = input("what is the capital of New Jersey?(a,b,c,d):")
#Correct answer:
correct_answer = ("a") #Trenton is the correct answer
#Check if the user's answer is correct
if user_answer == correct_answer:
    print("Correct!")
else:
    print("Incorrect.")

user_answer = input("Which nickname is often used to refer to New Jersey?(a,b,c,d:")
#Correct answer:
correct_answer = ("c")
#Check if the user's answer is correct
if user_answer == correct_answer:
    print("Correct")
else:
    print("Incorrect")

user_answer = input("How many lakes does Stockton University have?(a,b,c,d):")
#Correct answer:
correct_answer = ("d")
#Check if the user's answer is correct
if user_answer == correct_answer:
    print("correct")
else:
    print("incorrect")

user_answer = ("Who is the governor of New Jersey?(a,b,c,d):")
#Correct answer:
correct_answer = ("b")
#Check if the user's answer is correct(
if user_answer == correct_answer:
    print("correct")
else:
    print("incorrect")

user_answer = ("How many counties are in New Jersey?(a,b,c,d):")
#Correct answer:
correct_answer = ("c")
#Check if the user's answer is correct
if user_answer == correct_answer:
    print("correct")
else:
    print("incorrect")


# If the answer is correct, display a positive feedback message and add points to the user's score.
print("The user has succeeded and got all the question correct! Good Job!")
# If the answer is incorrect, display a negative feedback message and provide the correct answer.
print("The answer is incorrect. Try again!")
# Score Tracking:
#Question 1: 10
#Question 2: 15
#Question 3: 8
#Question 4: 20
#Question 5: 15

# Keep track of the user's score throughout the game.
# After all questions have been answered, display the user's total score and a farewell message.
total_score = "Congrats your total score was 68!"
# Function Utilization: 

# Create a function to ask a question and check the answer. This function should accept parameters like the question, options, and the correct answer, and return whether the user was correct.
# an example would be def ask_question(question, option_1, option_2, option_3, option_4, correct_answer):
def ask_question(question, option_1, option_2, option_3, option_4, correct_answer):
    print("What is the capital of New Jersey")
    print("a:", option_1)
    print("b:", option_2)
    print("c:", option_3)
    print("d:", option_4)
    correct_answer = "a"
    
    
# Keep track of the user's score throughout the game.
# After all questions have been answered, display the user's total score and a farewell message.
# Function Utilization:
# the return value should be a boolean (True or False) for whether the user was correct
if user_answer == correct_answer:
    Return: True
else:
    Return: False 
# Create a function to display the final score, which takes the score as a parameter and displays a message.
final_score = "68"
# Loops:
# Use a for or while loop to iterate through the questions.
# Variable Casting:
# Ensure that user input is cast and checked appropriately to avoid errors during execution.
# Error Handling:
# Implement basic error handling to manage invalid inputs from the user (e.g., an answer other than a, b, c, or d)
def user_input(error):
    while True:
        user_input = int(input("Enter your choice option 1, option 2, option 3, option 4"))
        if user_input in ("option 1, option 2, option 3, option 4"):
            return user_input
        else:
            print("Invalid input.")