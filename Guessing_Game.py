# attempting to generate a random number between 1 and 20 here

import random

print("I'm thinking of a number between one and twenty. Can you guess the number?")

random_integer = random.randint(1, 20)

while True:
    number = input('Please enter your best guess here: ')
    
    try:
        number = int(number)
    except ValueError:
        print("Please enter a valid integer.")
        continue  # Skip the rest of the loop and start a new iteration

    if 1 <= number <= 20:
        if number == random_integer:
            print("Well look at you, that is the right number.")
            break  # Exit the loop if the correct number is guessed
        else:
            print("Try again!")
    else:
        print("Please enter a number between 1 and 20.")
