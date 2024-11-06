"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Kateřina Marková
email: cathy.markova@gmail.com
discord: kate_marko1_54460
"""
import random
import time

print("Hi there!")
print(oddelovac := "-" * 48)
print("I've generated a random 4 digit number for you.\n"
      "Let's play a bulls and cows game.")
print(oddelovac)
def generate_secret_number():
    first_digit = random.choice(range(1, 10))   # První číslice nesmí být nula
    # Zbývající číslice mohou být libovolné mezi 0 a 9, ale ne stejné jako první číslice
    available_digits = [x for x in range(0, 10) if x != first_digit]
    other_digits = random.sample(available_digits, 3)
    secret_number = [first_digit] + other_digits
    return "".join(str(number) for number in secret_number)


# Ověření vstupu
def is_valid_input(user_choice):
    if not user_choice.isdigit():
        print("You must enter a number.")
        return False
    return True

def check_length(user_choice):
    if len(user_choice) != 4:
        print("You must enter a 4-digit number.")
        return False
    return True


def check_first_digit(user_choice):
    if user_choice.startswith("0"):
        print("Your number can't start with zero.")
        return False
    return True

def is_unique(user_choice):
    if len(user_choice) != len(set(user_choice)):
        print("Your digits must be unique.")
        return False
    return True

def calculate_bulls_and_cows(user_choice, sec_num):
    n_bull = sum(1 for i, number in enumerate(user_choice) if int(number) == int(sec_num[i]))
    n_cow = sum(1 for number in user_choice if number in sec_num) - n_bull
    return n_bull, n_cow

def play_game():
    sec_num = generate_secret_number()
    print(sec_num)
    start_time = time.time()
    guess_num = 0

    while True:
        user_choice = input(">>>  ")
        print(oddelovac)
        if not (is_valid_input(user_choice)
                and check_length(user_choice)
                and check_first_digit(user_choice)
                and is_unique(user_choice)):
            continue
        n_bull, n_cow = calculate_bulls_and_cows(user_choice, sec_num)
        bull = "bull" if n_bull == 1 else "bulls"
        cow = "cow" if n_cow == 1 else "cows"
        guess_num += 1
        if n_bull != 4:
            print(f"{n_bull} {bull}, {n_cow} {cow}")
        else:
            end_time = time.time()
            time_difference = end_time - start_time
            guess = "guess" if guess_num == 1 else "guesses"
            print(f"Correct, you've guessed the right number in {guess_num} {guess}!")
            print(f"Time taken: {time_difference:.2f} seconds")
            print(oddelovac)
            print("That's amazing!")
            return guess_num

# Statistiky
game_statistics = []
while True:
    print("Enter a number: ")
    print(oddelovac)
    guess_num = play_game()
    game_statistics.append(guess_num)
    total_num_games = len(game_statistics)
    attempts_per_game = sum(game_statistics) / total_num_games
    print(f"Total games played: {total_num_games}")
    print(f"Average attempts per game: {attempts_per_game:.2f}")

    while True:
        new_game = input("Do you want to play again? yes/no\n").strip().lower()
        if not new_game.isalpha():
            print("Enter an answer: yes/no")
            continue
        elif new_game.lower() == "yes":
            break

        elif new_game.lower() == "no":
            print("Thanks for playing.")
            exit()







