# HW8.py
# Author: Terrisha Edwards

# This homework will exapnd upon the code for Lab9.py. If you did not complete Lab9.py, you should do so before attempting this homework.

# Copy the code from Lab9.py into this file. I'll add some comments to help you out.

# Import statements (activate venv and install streamlit if you haven't already)
import streamlit as st
import datetime as dt  

# Streamlit title, subtitle, date, and button
st.title("My Streamlit App") 

def calcuate_days_until_birthday(birthday): 
    today = dt.date.today()
    next_birthday = dt.date(today.year, birthday.month, birthday.day)
    if today > next_birthday: dt.date (today.year + 1, next_birthday: 
        next_birthday = 
        dt.date(today.year + 1,birthday.month, birthday.day)
        delta = next_birthday - today 
        return delta.days   

# The calculate_days function from Lab9.py
def calcuate_days(date)
date = dt.datetime(date.yeat, date.month, date,day)
today = dt.datetime.now()
today = dt.datetime(today.year, today.month, today.day)
difference = date - today
return difference.days


# START OF HOMEWORK Questions
# 1. Create a function calculate_days_until_birthday that will calculate how many days from now until the user's birthday. The function should take in the user's birthday as a parameter and return the number of days until their birthday. The function should also display the number of days until their birthday in the Streamlit app. The function should be called in the app function.
import datetime as dt
import streamlit as st

def calculate_days_until_birthday(birthday): 
    today = dt.date.today()
    next_birthday = dt.date(today.year, birthday.month, birthday.day)
    if today > next_birthday:
        next_birthday = dt.date(today.year + 1, birthday.month, birthday.day)
    delta = next_birthday - today 
    return delta.days

def app():
    birthday = st.date_input('When is your birthday')
    days_until_birthday = calculate_days_until_birthday(birthday)
    st.write(f"Days until birthday: {days_until_birthday}")

if __name__ == '__main__':
    app()

# 2. Create a function days_until_semester_ends that will calculate how many days from now until the end of the semester. The function should take in the current date as a parameter and return the number of days until the end of the semester. The function should also display the number of days until the end of the semester in the Streamlit app. The function should be called in the app function.
# Hint: You can use the date object to create a date for the end of the semester. IE.
# end_of_semester = dt.date(2023, 12, 8)
import datetime as dt
import streamlit as st

def days_until_semester_ends(current_date):
    end_of_semester = dt.date(2023, 12, 8)
    delta = end_of_semester - current_date
    return delta.days

def app():
    current_date = dt.datetime.now().date()
    days_until_end_of_semester = days_until_semester_ends(current_date)
    st.write(f"Days until end of semester: {days_until_end_of_semester}")

if __name__ == '__main__':
    app()

# 3. Create a function days_until_new_years that will calculate how many days from now until New Year's Day. The function should take in the current date as a parameter and return the number 
# of days until New Year's Day. The function should also display the number of days until New Year's Day in the Streamlit app. The function should be called in the app function. Also include 
# an emoji of a party popper in the Streamlit app.
# Hint: You can use the date object to create a date for New Years. IE. 
# new_years = dt.date(2024, 1, 1)
# Hint: To add an emoji, use the st.write() function. IE. st.write("🎉")
import datetime as dt
import streamlit as st

def days_until_new_years(current_date):
    new_years = dt.date(current_date.year + 1, 1, 1)
    delta = new_years - current_date
    return delta.days

def app():
    current_date = dt.datetime.now().date()
    days_until_new_years_day = days_until_new_years(current_date)
    st.write(f"Days until New Year's Day: {days_until_new_years_day} 🎉")

if __name__ == '__main__':
    app()

# 4. create a button that will display the number of days until New Year's Day when clicked. The button should be labeled "Days until New Year's Day". The button should call the 
# days_until_new_years function when clicked. The button should be placed below the "Calculate" button.Inside the app function call the days_until_new_years function when the button is clicked.
import streamlit as st
import datetime as dt  

st.title("My Streamlit App") 

def calculate_days_until_birthday(birthday): 
    today = dt.date.today()
    next_birthday = dt.date(today.year, birthday.month, birthday.day)
    if today > next_birthday:
        next_birthday = dt.date(today.year + 1, birthday.month, birthday.day)
    delta = next_birthday - today 
    return delta.days

def days_until_semester_ends(current_date):
    end_of_semester = dt.date(2023, 12, 8)
    delta = end_of_semester - current_date
    return delta.days

def days_until_new_years(current_date):
    new_years = dt.date(current_date.year + 1, 1, 1)
    delta = new_years - current_date
    return delta.days

def app():
    birthday = st.date_input('When is your birthday')
    days_until_birthday = calculate_days_until_birthday(birthday)
    st.write(f"Days until birthday: {days_until_birthday}")

    current_date = dt.datetime.now().date()
    days_until_end_of_semester = days_until_semester_ends(current_date)
    st.write(f"Days until end of semester: {days_until_end_of_semester}")

    if st.button("Days until New Year's Day"):
        days_until_new_years_day = days_until_new_years(current_date)
        st.write(f"Days until New Year's Day: {days_until_new_years_day} 🎉")

if __name__ == '__main__':
    app()

# Hint: You can use the st.button() function. IE. button = st.button("Click me")
# Hint2: the days_until_new_years function takes in the current date as a parameter. You can use the dt.datetime.now().date() function to get the current date. 
# IE. current_date = dt.datetime.now().date()
# Hint3: You can use the days_until_new_years function to get the number of days until New Year's Day. IE. days_until_new_years(current_date) This is where you include the emoji  🎉


# app function from Lab9.py



if __name__ == '__main__':
    app()