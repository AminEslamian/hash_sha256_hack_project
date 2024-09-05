# Import necessary modules
from hashlib import sha256  # For hashing
import random  # For generating random numbers
import string  # For accessing characters

# Define a constant for the target hash value
pass_hash = '7902699be42c8a8e46fbbb4501726517e86b22c56a189f7625a6da49081b2451'

# Function to generate a random word of specified length
def generate_random_word(length):
    # Create a string containing all possible characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random word by randomly selecting characters from the string
    random_word = ''.join(random.choice(characters) for _ in range(length))

    return random_word

# Create an empty dictionary to store hashed words and their corresponding plain text
pass_dict = dict()

# Function to create a dictionary of hashed words
def hassh_dict_creator(length, num):
    # Iterate through the specified number of iterations
    for i in range(1, num+1):
        # Calculate the percentage of completion
        percentage = (i / num) * 100

        # Print the progress percentage; if you want to have numbers like 11.20% instead 11.2% change 1f to 2f
        print(f"Progress: {percentage:.1f}%")

        # Generate a random word of the specified length
        random_word = generate_random_word(length)

        # Check if the generated random word's hash is already in the dictionary
        if random_word not in pass_dict.values():

            hassed = sha256(random_word.encode('utf-8')).hexdigest() # Hash the random word

            # Add the hashed word and its corresponding plain text to the dictionary
            pass_dict[hassed] = random_word

# Get user input for password length and number of iterations
input1 = int(input('how many characters does the password has? '))
input2 = int(input('how many times do you want the process to be looped?'))

# Call the function to create the dictionary of hashed words
hassh_dict_creator(input1, input2)

# Check if the target hash is found in the dictionary
if pass_hash in pass_dict.keys():
    # Print the corresponding plain text password
    print(pass_dict[pass_hash])
else:
    # Print a message indicating that the password was not found
    print('Not Found!')