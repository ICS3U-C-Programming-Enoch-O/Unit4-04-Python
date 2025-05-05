#!/usr/bin/env python3
# Created by: Enoch O
# Created on: April 22, 2025

import random


def main():
    # Generates random number between 0-9
    random_numb = random.randint(0, 9)


    #loops until you guess correctly
    while True:
        user_numb_guess = input("guess a number between (0-9): ")


        # tries to convert user input into interger
        try:
            user_numb_guess_int = int(user_numb_guess)


            # Checks if user guess within the range
            if user_numb_guess_int < 0 or user_numb_guess_int > 9:
                print(f"{user_numb_guess_int} is not between 0 and 9")


            # If guessed correctly it stops the loop
            elif user_numb_guess_int == random_numb:
                print(f"{user_numb_guess_int} is the correct guess!!!")
                break


            # If not it continues the loop
            else:
                print("bad guess, try harder")


        # catches the error that occurs when converting doesn't work
        except Exception:
            print(f"{user_numb_guess} is not an integer")


    print("Thanks for playing")


if __name__ == "__main__":
    main()
