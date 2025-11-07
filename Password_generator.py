# ask user How long the password should be . 
# what characters to include. ( numbers, symbols etc )
# generate a random passwords based on these info. 
# show the password to user. 

#? INPUT TO TAKE 
        #=> password length, allowed character type. 
#* Process => randomly choose characters from the alphabet. 
#! Ouput => Final program string. 

import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()_+[]{}"

length = int(input("Enter your password length: "))

include_letters = input("Include Letters? (y/n): ").lower()
include_numbers = input("Include numbers? (y/n): ").lower()
include_symbols = input("Include symbols? (y/n): ").lower()

allowed_chars = ""
if include_letters == "y":
    allowed_chars += letters
if include_numbers == "y":
    allowed_chars += numbers
if include_symbols == "y":
    allowed_chars += symbols

if allowed_chars == "": 
    print("You must select at least one thing! ")

password = "".join(random.choice(allowed_chars) for _ in range(length))
print(password)
print(random.choice(allowed_chars) )


#I understand about random module in it. 
#.join is a string method used to join characters.  works on iterable items

# _ this is a throwaway varaible name( convention ) -> use it when you just want to repeat something. 
# for _ in range(3). range is a function starts from zero and goes to 3 ( not included)
