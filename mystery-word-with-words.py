import random
import os
import sys

from black import diff

file = open("words.txt")
file
randomed = ""
the_random = ""
wordle = ""
by_length = dict()
difficulty = input(
    "What difficulty level would you like: Easy, Normal, or Hard? ").title()

difficulties = ["Easy", "Normal", "Hard"]

while difficulty not in difficulties:
    if difficulty not in difficulties:
        print("Please check you're spelling and try again.")
        difficulty = input(
            "What difficulty level would you like: Easy, Normal, or Hard? ").title()
    elif difficulty in difficulties:
        break


def random_word(file):
    global wordle
    randomed = file.readlines()
    the_random = [word.upper().strip() for word in randomed]
    by_length = dict()
    for word in the_random:
        by_length[word] = len(word)
    if difficulty == "Easy":
        wordle = random.choice(
            list({k: v for (k, v) in by_length.items() if v >= 4 and v <= 6}))
    elif difficulty == "Normal":
        wordle = random.choice(
            list({k: v for (k, v) in by_length.items() if v >= 6 and v <= 8}))
    elif difficulty == "Hard":
        wordle = random.choice(
            list({k: v for (k, v) in by_length.items() if v >= 8}))
    return wordle, print(f"Your word has {len(wordle)} letters.", wordle)


print(wordle)

random_word(file)

word_guess = input("Guess the word: ")
word_count = 0

while len(word_guess) != len(wordle):
    if len(word_guess) != len(wordle):
        print(word_guess)
        print("Please check you're spelling and word length and try again")
        word_guess = input(
            "Guess the word: ")
    elif len(word_guess) == len(wordle):
        break

if word_guess != "":
    word_count += 1

current_guesses = list(word_guess.upper())

print(word_count)


def display_letter(letter, guesses):
    guessed = []
    if letter in guesses:
        guessed += letter
        return letter
    else:
        guessed += "-"
        return "_"


output_letters = []


def print_word(wordle, guesses):
    global output_letters
    output_letters = [display_letter(letter, guesses)
                      for letter in wordle]
    print(" ".join(output_letters))


[display_letter(letter, current_guesses) for letter in wordle]
print_word(wordle, current_guesses)


if " ".join(output_letters).replace(" ", "") == wordle:
    print("Correct! You got it!")
    restart = input("\nDo you want to restart the Game? [y/n] > ")
    if restart == "y":
        os.execl(sys.executable, sys.executable,
                 os.path.abspath(__file__), *sys.argv)
    else:
        print("\nGoodbye, thanks for playing!")
        sys.exit(0)


while word_count != 9:
    try:
        word_guess = input("Guess the word: ")
        current_guesses = list(word_guess.upper())
        print_word(wordle, current_guesses)
        "".join(output_letters)
        if word_count == 8:
            print("Sorry, better luck next time!")
            restart = input("\nDo you want to restart the Game? [y/n] > ")
            if restart == "y":
                os.execl(sys.executable, sys.executable,
                         os.path.abspath(__file__), *sys.argv)
            else:
                print("\nGoodbye, thanks for playing!")
                sys.exit(0)
        if "".join(output_letters) == wordle:
            print("Correct! You got it!")
            restart = input("\nDo you want to restart the Game? [y/n] > ")
            if restart == "y":
                os.execl(sys.executable, sys.executable,
                         os.path.abspath(__file__), *sys.argv)
            else:
                print("\nGoodbye, thanks for playing!")
                sys.exit(0)
        else:
            while len(word_guess) != len(wordle):
                if len(word_guess) != len(wordle):
                    print(word_guess)
                    print("Please check you're spelling and word length and try again")
                    word_guess = input("Guess the word: ")
                elif len(word_guess) == len(wordle):
                    break
            print(" ".join(output_letters))
            print("Not quite! Try again!")
            current_guesses = []
            current_guesses = list(word_guess.upper())
            word_count += 1
            print(word_count)
            print_word(wordle, current_guesses)
            print("".join(output_letters))
            print(wordle)
    except ValueError:
        print("Provide an integer value...")
        continue
