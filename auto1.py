# import random
#
# def play_guessing_game():
#     secret_number = random.randint(1, 100)
#     attempts = 0
#
#     print("Welcome to the Guessing Game!")
#     print("I'm thinking of a number between 1 and 100.")
#
#     while True:
#         guess = int(input("Take a guess: "))
#         attempts += 1
#
#         if guess < secret_number:
#             print("Too low!")
#         elif guess > secret_number:
#             print("Too high!")
#         else:
#             print(f"Congratulations! You guessed the number in {attempts} attempts!")
#             break
#
#     print("Thanks for playing!")
#
# play_guessing_game()



# import random
#
# def play_letter_guessing_game():
#     words = ['apple', 'banana', 'carrot', 'durian', 'eggplant', 'fig', 'grape']
#     secret_word = random.choice(words).lower()
#     guessed_letters = []
#     attempts = 6
#
#     print("Welcome to the Letter Guessing Game!")
#     print("Try to guess the letters in the secret word.")
#
#     while attempts > 0:
#         display_word = ''
#         for letter in secret_word:
#             if letter in guessed_letters:
#                 display_word += letter
#             else:
#                 display_word += '_'
#
#         print("\nSecret Word:", display_word)
#         print("Attempts Left:", attempts)
#         print("Guessed Letters:", guessed_letters)
#
#         guess = input("Enter a letter: ").lower()
#
#         if len(guess) != 1 or not guess.isalpha():
#             print("Invalid input. Please enter a single letter.")
#             continue
#
#         if guess in guessed_letters:
#             print("You already guessed that letter.")
#             continue
#
#         guessed_letters.append(guess)
#
#         if guess in secret_word:
#             print("Correct guess!")
#         else:
#             print("Wrong guess!")
#             attempts -= 1
#
#         if '_' not in display_word:
#             print("\nCongratulations! You guessed the word:", secret_word)
#             break
#
#     if attempts == 0:
#         print("\nGame over! You ran out of attempts. The secret word was:", secret_word)
#
#     print("\nThanks for playing!")
#
# play_letter_guessing_game()

import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guessing Game")

        self.number_to_guess = random.randint(1, 5)
        self.remaining_attempts = 5

        self.label = tk.Label(master, text="Guess a number between 1 and 5:")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Guess", command=self.check_guess)
        self.button.pack()

        self.remaining_attempts_label = tk.Label(master, text=f"Remaining attempts: {self.remaining_attempts}")
        self.remaining_attempts_label.pack()

    def check_guess(self):
        guess = int(self.entry.get())

        if guess == self.number_to_guess:
            messagebox.showinfo("Result", "Congratulations! You guessed correctly.")
            self.master.destroy()
        else:
            self.remaining_attempts -= 1
            if self.remaining_attempts == 0:
                messagebox.showinfo("Result", f"Game Over. The number was {self.number_to_guess}.")
                self.master.destroy()
            else:
                messagebox.showinfo("Result", f"Wrong guess. Try again. Remaining attempts: {self.remaining_attempts}")
                self.remaining_attempts_label.config(text=f"Remaining attempts: {self.remaining_attempts}")

        self.entry.delete(0, tk.END)

root = tk.Tk()
game = GuessingGame(root)
root.mainloop()

