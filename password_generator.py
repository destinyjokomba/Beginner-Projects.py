#Import modules
import random 
import string

#Ask user for minimal length 
def generate_password(min_Length, numbers=True, special_characters=True): #parameters start with the minimum length of the password which have options if the user wants to add any specail characters or numbers
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation
    
#Combine to one large list that users can randomly chose from 
    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = "" #Password is empty 
    meet_criteria = False 
    has_number = False
    has_special = False 

#If the users password does not have a number or special character and does not meet the min length required for the password keep adding until it does
    while not meet_criteria or len(pwd) < min_Length: #If either of these statements are true then continue loop
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

#Update meets criteria 
        meet_criteria = True
        if numbers:
            meet_criteria = has_number
        if special_characters: 
            meet_criteria = meet_criteria and has_special #AND expression only returns True if the condition on the left and the right are true 

    return pwd         


#User input 
min_Length =int(input ("Enter the minimum length: ")) #Ask user minimum length and convert into int 
has_number = input("Would you like to include numbers (yes/no)? ").lower() == "yes"
has_special = input("Would you like to include speical characters (yes/no)? ").lower() == "yes"
pwd = generate_password(min_Length, has_number, has_special)
print("The password generated for you is ", pwd)