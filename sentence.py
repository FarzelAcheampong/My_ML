# # def shuffle(string):
# i_input = input("Type a sentence:")
#
# f_input = input("\nType a word in or out of the  sentence:")
#
# if f_input in i_input:
#
#     print("\nTrue".upper())
#
# else:
#
#     print("\nthere is no such word in the sentence".upper())
import random
def guessgame():
    number = random.randint(1, 5)
    tries = 0

    while True:
        guess = int(input('Enter a number:'))
        tries += 1

        if guess < number:
            print('Guess is too Low')
        elif guess > number:
            print('Guess is too high')
        elif guess != number:
            print('Guess must be a number.')
        else:
            print(f"You guessed the number with {tries} tries")
            break
guessgame()



