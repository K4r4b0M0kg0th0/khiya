# A program that generates a random password based on some criteria

# Import the random module
import random

# Define the characters that can be used in the password
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
symbols = "!@#$%^&*()_+-=[]{};:,./<>?"

# Ask the user for the length of the password
length = int(input("Enter the length of the password: "))

# Ask the user if they want to include lowercase letters
lower = input("Do you want to include lowercase letters? (y/n): ")

# Ask the user if they want to include uppercase letters
upper = input("Do you want to include uppercase letters? (y/n): ")

# Ask the user if they want to include digits
digit = input("Do you want to include digits? (y/n): ")

# Ask the user if they want to include symbols
symbol = input("Do you want to include symbols? (y/n): ")

# Create an empty string to store the possible characters
chars = ""

# Add the lowercase letters to the possible characters if the user wants them
if lower == "y":
  chars += lowercase

# Add the uppercase letters to the possible characters if the user wants them
if upper == "y":
  chars += uppercase

# Add the digits to the possible characters if the user wants them
if digit == "y":
  chars += digits

# Add the symbols to the possible characters if the user wants them
if symbol == "y":
  chars += symbols

# Check if the possible characters are not empty
if chars != "":
  # Create an empty string to store the generated password
  password = ""

  # Loop for the length of the password
  for i in range(length):
    # Choose a random character from the possible characters and add it to the password
    password += random.choice(chars)

  # Print the generated password
  print("Your password is:", password)

else:
  # Print an error message if the possible characters are empty
  print("You have not selected any characters for your password.")