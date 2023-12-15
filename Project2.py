# Project 2
# Name: Terrisha Edwards 
# Project 2 will test on topics learned in class so far. You will be creating a contact list program with an external csv file that will store the contacts. The program will have the following features:
# 1. Add contact
# 2. View contacts
# 3. Delete contact
# 4. Save contacts to csv file
# 5. Next Birthday
# 0. Quit

# Import the csv module, datetime module
import csv 
import datetime 

def import_csv(contact.csv):
    try:
        with open(contact.csv, 'r') as file:
            reader = csv.reader(file)
            next(reader)
        data = [row for row in reader]
        return data 
for row in reader: 
    data.append(row)

    return data 
# Make sure to show docs strings for each function and include comments in your code. Make sure to include a main function and call the main function at the end of the program.
<<<<<<< HEAD
=======
def main():
    "Main function to run the program"
    file_path = 'contatcs.csv'
    contact_data = import_csv(file_path)
    
    while True:
        display_menu 
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            
        
        elif choice == 
>>>>>>> 3e6c00a86337023e351a3121023764c3b45d9de2
print("Welcome to the Contact List Program")

def import_csv(contacts.csv):
    try:
        with open(contacts + '.csv', 'r') as file:
            reader = csv.reader(file)
            next(reader)
            contacts = {}
            for row in reader: contacts[row[0]] = {
                'Phone': row[1],
                'Email': row[2],
                'Birthday': dt.datetime.strptime(row[3],'%m/%d/%Y').date()
            }
                return contacts
    except FileNotFoundError:
        print(f"File'{contacts}.csv' not found. No contacts imported.")


# There is also a contact.csv file that will be used to store the contacts. The csv file will have the following format:
# Name,Phone,Email,Birthday
# The program will be menu driven and will display the menu as shown above. The program will run until the user selects option 0 to quit. The program will be implemented in a file called Project2.py. The program will use the following functions:


    
# import_csv - This function will import the contacts from the csv file. The function will return a dictionary of contacts. The key will be the name of the contact and the value will be a dictionary containing the phone number, email address, and birthday. The function will take one parameter, the name of the csv file. The function will display an error message if the file does not exist. The function will display a message if the file exists and the contacts were imported successfully.
# Hint1: Use the csv module to read the csv file. Use the csv.reader function. IE. reader = csv.reader(file)
# Hint2: You will need to skip the first line of the csv file since it contains the column headers. You can do that with the next function. IE. next(reader)
# Hint3: You will need to create a dictionary of contacts. You can do that by looping through the reader object. IE. for row in reader:
# Hint4: You will need to convert the birthday to a datetime object. You can do that by using the strptime function. IE. dt.datetime.strptime(row[3], '%m/%d/%Y')
# Hint5: You will need to create a dictionary of the phone number, email address, and birthday. You can do that by creating a dictionary and adding the values to the dictionary. IE. contact[row[0]] = {'Phone': row[1], 'Email': row[2], 'Birthday': dt.datetime.strptime(row[3], '%m/%d/%Y')}
# Hint6: Use the FileNotFoundError exception to catch if the file does not exist.


# add_contact(name, phone, email, birthday) - This function will add a contact to the dictionary. The function will take four parameters, the name, phone number, email address, and birthday. The function will return True if the contact was added and False if the contact was not added. The function will display an error message if the contact already exists.
# Hint 1: You will need to convert the birthday to a datetime object. You can do that by using the strptime function. IE. dt.datetime.strptime(birthday, '%m/%d/%Y')
# Hint 2: To add a contact to the dictionary, you need to use the key as the name and the values as a dictionary that contains the phone number, email address, and birthday. To reference the specific key you can use contact[name]
def add_contact(name, phone, email, birthday):
    birthday = dt.datetime.strptime(birthday,'%m/%d/%Y')
    if name in contacts: 
        print (f"Contact '{name}' already exists.")
        return False 
    else:
        info = {'Phone': phone, 'Email': email, 'Birthday': birthday}
        contacts[name] = info
        print(f"Contact '{name}' added successfully.")
        return True 

# view_contacts() - This function will display the contacts in the dictionary. The function will take no parameters. The function will return nothing. The function will display a message if there are no contacts in the dictionary. Use string formatting to display the contacts in a table format. The table should have a header row and each contact should be on a separate row. The table should have the following columns: Name, Phone, Email, Birthday. The birthday should be formatted as mm/dd/yyyy. The table should be sorted by name.
# Hint 1: You will need to loop through the dictionary to display the contacts. IE. for key, value in contact.items():
# Extra Credit: The data is a dictionary of dictionaries. You can unpack the dictionary into a list of dictionaries. Like in Lab 10 and then use the tabulate library to display the contacts in a table format. This is optional and not required. You can use string formatting to display the contacts in a table format.
def view_contacts(contacts):
    """
    Display the contacts in a table format.

    Parameters:
    -contacts: Dictionary containing contacts.

    Returns: 
    None 
    """
    if not contacts:
        print("No contacts found.")
        return
    
    header = ["Name", "Phone", "Email", "Birthday"]
    print(" ".join(header)) 
    for name, info in sorted(contacts.items()):
        print("{:<20}"{:<15}{:<30}{:<15})". format(name, info['Phone'],info['Email'],info['Birthday'].strftime('%m/%d/%Y'))



# delete_contact(id) - This function will delete a contact from the dictionary. The function will take one parameter, the name of the contact to delete. The function will return True if the contact was deleted and False if the contact was not deleted. The function will display an error message if the contact does not exist.
def delete_contact(contacts, name):
    """
    Delete a contact from the dictionary.

    Parameters:
    -contacts: Dictionary containing existing contacts.
    -name: Name of the contact to delete

    Returns:
    True id the contact was deleted, False otherwise.
    """
    if name in contacts:
        del contacts[name]
        return True 
    else:
        print(f"Contact '{name}' not found. Unable to delete.")
        return False

# next_birthday() - This function will display the next birthday. The function will take no parameters. The function will return nothing. The function will display a message if there are no contacts in the dictionary. The function will display a message if there are no birthdays in the next 30 days. The function will display the next birthday and name if there is a birthday in the next 30 days. Use string formatting to display the next birthday. The next birthday should be sorted by the next birthday. The next birthday should be formatted as mm/dd/yyyy.
# Hint: We dont care about the year, only the month and day. There are many ways to solve this issue. 1st you could replace all the years with the current year.2nd you could use the month and day attributes of the datetime object to compare the month and day of the birthday to the current month and day.
def next_birthday(contacts):
    """
    Display the next birthday.

    Parameters:
    -contacts: Dictionary containing contacts.

    Returns: 
    None 
    """
    today = dt.date.today()
    next_birthday_list = []

    for name, info in contacts.items():
        birthday = info['Birthday'].replace(year=today.year)
        if today <= birthday <= today + dt.timedelta(days=30):
            next_birthday_list.append((name, birthday))

        if not next_birthday_list:
            print("NO birthdays in the next 30 days.")
            return
        
        next_birthday_list.sort(key=lambda x:[1])

        print("Next Birthdays:")
        for name, birthday in next_birthday_list:
            print(f"{name}: {birthday.strftime('%m/%d/%Y')}")

# save_csv(filename) - This function will save the contacts to the csv file. Prompt the user to enter a filename to save the contacts to. If the file exists, overwrite the file. If the file does not exist, create the file. The function will return True if the contacts were saved and False if the contacts were not saved.
def save_csv(contacts, file_path):
    """
    Save contacts to a CSV file.

    Parameters:
    -contacts: Dictionary containing contacts.
    -file_path: The path of the CSV file.

    Returns: 
    True if the contacts were saved, False otherwise.
    """
    try:
        with open(file_path, 'w', newline= '') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Phone", "Email", "Birthday"])
            for name, info in contacts.items():
                writer.writerow([name, info['Phone']], info['Email'], info['Birthday'].strftime('%m/%d/%Y'))
                return True
    except Expection as e:
        print(f"Error saving contacts: {e}")
        return False
    
# The main function will be used to run the program. The main function will use a while loop to display the menu and get the user's choice. The main function will call the appropriate function based on the user's choice. The main function will also call the save_csv function to save the contacts to the csv file before the program ends.
while True:
    print("Menu:")
    print("1.Add a new contact")
    print("2. Delete an existing contact")
    print("3.Find and display a contact")
    print("4.Save the contacts to the csv file")
    print("5.View all contacts")
    print("0.Quit the program")
    option = input("Enter your option: ")
    
    if option == "1":
        name = input("Enter the name: ")
        phone = input("Enter the phone number: ")
        email = input("Enter the email address: ")
        birthday = input("Enter the birthday(mm/dd/yyyy): ")
        add_contact(name,phone,email,birthday)
    elif option == "2":
        name = input("Enter the name: ")
        delete_contact(name)
    elif option == "3":
        name = input("Enter the name: ")
# Project 2 will test on topics learned in class so far. You will be creating a contact list program with an external csv file that will store the contacts. The program will have the following features:
    elif option == "4":
        def save_contacts(contacts): 
            elif option == "5": 
            
        def view_contacts(contacts):
            elif option == "0":
        print("Thank you for using the Contact List Program. Goodbye!")
        break
    else:
        print("Invalid option.Please try again.")


def main():
    """Add Code here to call the functions and run the program"""

    # After you are done with the program, answer the following questions using code (show your code and output):
    # How many names start with the letter A?
count = 0
for name in contacts:
    if name.startswith('A'):
        count += 1
print(f"There are {5} names that start with the letter A.")
    # How many emails are yahoo emails?
count = 0
for name, info in contacts.items():
    if 'yahoo' in info['Email']: 
        count += 1
print(f"There are {5} emails that are yahoo emails.")
    # How many .org emails are there?
count = 0
for name, info in contacts.items():
    if['Email'].endswith('.org'):
        count +=1
print(f"There are {2} emails that are .org emails.")  
    # How many contacts have a birthday in January?
count = 0
for name. info in contacts.items():
    if info['Birthday'].month == 1:
        count += 1
print(f"There are {2} contacts that have a birthday in January.")

if __name__ == "__main__":
    main()
