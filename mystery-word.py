from black import diff
from click import style
from colorama import init
from colorama import Fore, Back, Style
import random
import os
import sys
init()
file = open("words.txt")
file
randomed = ""
the_random = ""
wordle = ""
by_length = dict()
print(Fore.WHITE + Style.BRIGHT + Back.MAGENTA +
      "Welcome to my word game, let's have a play! ʕʘ̅͜ʘ̅ʔ ")
difficulty = input(
    "What difficulty level would you like: Easy, Normal, or Hard? ").title()

difficulties = ["Easy", "Normal", "Hard"]

while difficulty not in difficulties:
    if difficulty not in difficulties:
        print(Fore.WHITE + Style.BRIGHT +
              Back.BLUE + "Please check you're spelling and try again.")
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
    return wordle, print(Fore.YELLOW + Style.BRIGHT + Back.RED + f"Great! Your word has {len(wordle)} letters. \nPlease guess only one Letter at a time.")


random_word(file)

word_guess = input(Fore.WHITE + Style.BRIGHT +
                   Back.BLUE + "Guess a Letter: ").upper()
word_count = 0
if len(word_guess) > 1:
    print(Fore.WHITE + Style.BRIGHT + Back.MAGENTA +
          "Input invalid, please enter one letter at a time.")
    word_guess = ""


if word_guess not in wordle:
    word_count += 1
    print("Sorry Letter not in the word.")
elif word_guess in wordle:
    word_count = 0


current_guesses = list(word_guess)

print(Fore.YELLOW + Style.BRIGHT + Back.RED +
      "No. of Guesses: " + str(word_count))


def display_letter(letter, guesses):
    global guessed
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

#print_word(wordle, current_guesses)

if " ".join(output_letters).replace(" ", "") == wordle:
    print(Fore.WHITE + Style.BRIGHT +
          Back.BLUE + "Correct! You win!")
    restart = input("\nDo you want to restart the Game? [y/n] > ")
    if restart == "y":
        os.execl(sys.executable, sys.executable,
                 os.path.abspath(__file__), *sys.argv)
    else:
        print("\nGoodbye, thanks for playing!")
        sys.exit(0)


while word_count != 9:
    try:
        current_guesses = list(word_guess)
        print_word(wordle, current_guesses)
        if word_count == 8:
            print("Sorry, better luck next time!" + "  ¯\_(ツ)_/¯ ")
            restart = input("\nDo you want to restart the Game? [y/n] > ")
            if restart == "y":
                os.execl(sys.executable, sys.executable,
                         os.path.abspath(__file__), *sys.argv)
            else:
                print("\nGoodbye, thanks for playing!")
                sys.exit(0)
        if "".join(output_letters) == wordle:
            print(Fore.WHITE + Style.BRIGHT +
                  Back.BLUE + "Correct! You win!  q(❂‿❂)p  ⊂(◉‿◉)つ ")
            restart = input("\nDo you want to restart the Game? [y/n] > ")
            if restart == "y":
                os.execl(sys.executable, sys.executable,
                         os.path.abspath(__file__), *sys.argv)
            else:
                print("\nGoodbye, thanks for playing!")
                sys.exit(0)
        else:
            typed = input("Guess a Letter: ").upper()
            if len(typed) > 1:
                print(Fore.WHITE + Style.BRIGHT + Back.MAGENTA +
                      "Input invalid, please enter one letter at a time.")
                typed = ""
            elif typed in word_guess:
                print(Fore.WHITE + Style.BRIGHT +
                      Back.BLUE +
                      'You already guessed this yo ')
                print(Fore.YELLOW + Style.BRIGHT + Back.RED +
                      "No. of Guesses: " + str(word_count))
            elif typed not in word_guess and typed in wordle:
                word_guess += typed
                current_guesses = list(word_guess)
                print(Fore.YELLOW + Style.BRIGHT + Back.RED +
                      "No. of Guesses: " + str(word_count))
            else:
                word_guess += typed
                current_guesses = list(word_guess)
                word_count += 1
                print(Fore.WHITE + Style.BRIGHT + Back.MAGENTA + "Sorry Letter not in the word."
                      + "\nNo. of Guesses: " + str(word_count))

                #print_word(wordle, current_guesses)
                # print("".join(output_letters))
                # print(wordle)
    except ValueError:
        print("Please provide a letter")
        continue
