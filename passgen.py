import random
import string

#letters = string.ascii_lowercase #lowercase
letters = string.ascii_letters #mixed case

password_string = ""
password_length = int(input("Enter length of password:"))
include_special = input("Use special characters (y/n)").lower().strip()
include_numbers = input("Include numbers (y/n)").lower().strip()

special_characters = ["!", "@", "#", "$", "?"]

if include_special[0] == "y":
    if include_numbers[0] == "y":
        for i in range(password_length-2):
            password_string += random.choice(letters) # repeat characters allowed
            
        password_string += str(random.randint(0,9))
    else:
        for i in range(password_length-1):
            password_string += random.choice(letters) 
            
    password_string += random.choice(special_characters)
else:
    if include_numbers[0] == "y":
        for i in range(password_length-1):
            password_string += random.choice(letters)

        password_string += str(random.randint(0,9))
    else:
        for i in range(password_length
                       ):
            password_string += random.choice(letters)

print(password_string)
        