# A program that generates a random password based on some criteria

# Import the random and string modules
import random
import string

# Define the characters that can be used in the password
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
symbols = string.punctuation

# Ask the user for the length of the password and convert it to an integer
length = input("Enter the length of the password: ")

# Use a loop to validate the length of the password
while True:
  # Try to convert the length to an integer
  try:
    length = int(length)
    # Check if the length is positive
    if length > 0:
      # Break out of the loop if the length is valid
      break
    else:
      # Print an error message if the length is not positive
      print("The length of the password must be a positive integer.")
  except ValueError:
    # Print an error message if the length is not an integer
    print("The length of the password must be an integer.")

  # Ask the user again for the length of the password
  length = input("Enter the length of the password: ")

# Ask the user for the types of characters they want to include and convert them to booleans
lower = input("Do you want to include lowercase letters? (y/n): ") == "y"
upper = input("Do you want to include uppercase letters? (y/n): ") == "y"
digit = input("Do you want to include digits? (y/n): ") == "y"
symbol = input("Do you want to include symbols? (y/n): ") == "y"

# Create a list to store the possible characters
chars = []

# Add the lowercase letters to the possible characters if the user wants them
if lower:
  chars.extend(lowercase)

# Add the uppercase letters to the possible characters if the user wants them
if upper:
  chars.extend(uppercase)

# Add the digits to the possible characters if the user wants them
if digit:
  chars.extend(digits)

# Add the symbols to the possible characters if the user wants them
if symbol:
  chars.extend(symbols)

# Check if the possible characters are not empty
if chars:
  # Generate a random password from the possible characters and join it into a string
  password = "".join(random.choices(chars, k=length))

  # Print the generated password
  print("Your password is:", password)

else:
  # Print an error message if the possible characters are empty
  print("You have not selected any characters for your password.")