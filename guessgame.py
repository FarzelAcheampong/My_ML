import random

def guessing_game():

    number = random.randint(1, 4)
    tries = 0

    print("Welcome to my guessing game")
    print("I am thinking of a number")
    print("Can you guess the number")

    while True:
        guess = int(input("Enter your number:"))
        tries += 1

        if guess < number:
            print("Too low, try again!")
        elif guess > number:
            print("Too high, try again!")
        elif guess != number:
            print("Guess a number not a letter!")
        # elif tries == 1:
        #     print(f"Congratulations you guessed the number with {tries} try")

        else:
            print(f"Congratulations you guessed the number with {tries} tries")
            break

guessing_game()

