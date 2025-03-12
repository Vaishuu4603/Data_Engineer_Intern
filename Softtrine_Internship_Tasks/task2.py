# Task 2: Number Guessing Game
# 1. Generates a random number between 1 and 50.
# 2. Asks the user to guess the number.
# 3. Gives hints like "Too High" or "Too Low" until the user guesses correctly.
# 4. Displays how many attempts it took to guess the number.


import random
randNum=random.randint(1,50)
guess=0
attempts=0
while guess!=randNum:
    attempts = attempts + 1
    guess=int(input("Guess the number(1-50)-> "))

    if guess == randNum:
        print("number was",randNum)
        print("Guess is correct!!!")
        break
    elif guess > randNum:
        print("Guess is too high")
    else:
        print("Guess is too low")
print("total attempts: ",attempts)


# Output:

# Guess the number(1-50)-> 15
# Guess is too low
# Guess the number(1-50)-> 25
# Guess is too low
# Guess the number(1-50)-> 35
# Guess is too low
# Guess the number(1-50)-> 45
# Guess is too high
# Guess the number(1-50)-> 44
# Guess is too high
# Guess the number(1-50)-> 43
# Guess is too high
# Guess the number(1-50)-> 42
# Guess is too high
# Guess the number(1-50)-> 41
# Guess is too high
# Guess the number(1-50)-> 40
# Guess is too high
# Guess the number(1-50)-> 39
# number was 39
# Guess is correct!!!
# total attempts:  10