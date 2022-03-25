import sys
import random


def guessing_game(num1, num2):
    random_number = random.randint(int(num1), int(num2))
    guess = input(f"Guess the number between {num1} and {num2}! ")
    while True:
        try:
            if int(num1) <= int(guess) <= int(num2):
                if int(guess) != random_number:
                    print("Nope, that's not it! ")
                    guess = input("Guess again! ")
                    continue
                else:
                    print('That is correct! You\'re an amazing detective/genius!')
                    break
            else:
                guess = input(
                    f"That's not between {num1} and {num2}, please enter a new number! ")
                continue

        except ValueError:
            guess = input("Please enter a number! ")
            continue


# extracted a part of the code as a function so that it can be tested

# def guessing(guess, random_number):
#     if int(num1) <= int(guess) <= int(num2):
#         if int(guess) != random_number:
#             print("Nope, that's not it! ")
#             guess = input("Guess again! ")
#             return
#         else:
#             print('That is correct! You\'re an amazing detective/genius!')
#             return
#     else:
#         guess = input(
#             f"That's not between {num1} and {num2}, please enter a new number! ")
#         return


# if __name__ == '__main__':
#     def guessing_game(num1, num2):
#         random_number = random.randint(int(num1), int(num2))
#         guess = input(f"Guess the number between {num1} and {num2}! ")
#         while True:
#             try:
#                 guessing(guess, random_number)


#             except ValueError:
#                 guess = input("Please enter a number! ")
#                 continue


guessing_game(sys.argv[1], sys.argv[2])
