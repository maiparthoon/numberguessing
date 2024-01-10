import random

print("WELCOME TO YOUR NUMBER GUESSING GAME!!!!!")

while True:
    dificulties = {
        "easy": {"lower_limit": 0, "upper_limit": 20, "max_attempts": 5},
        "medium": {"lower_limit": 0, "upper_limit": 50, "max_attempts": 15},
        "hard": {"lower_limit": 0, "upper_limit": 100, "max_attempts": 20},
    }

    chosen_dificulty = input("Select a dificulty (easy, medium, hard): ").lower()

    while chosen_dificulty not in dificulties:
        print("Invalid dificulty chosen. Please choose from easy, medium or hard..")
        chosen_dificulty = input("Select a dificulty (easy, medium, hard): ").lower()

    lower_limit = dificulties[chosen_dificulty]["lower_limit"]
    upper_limit = dificulties[chosen_dificulty]["upper_limit"]
    max_attempts = dificulties[chosen_dificulty]["max_attempts"]

    secret_number = random.randint(lower_limit, upper_limit)

    attempts = 0

    while attempts < max_attempts:
        guess = int(input(f"What is your guess? Choose from between {lower_limit} and {upper_limit}: "))
        attempts += 1

        if guess == secret_number:
            print(f"Congrats, You have guessed it correctly in {attempts} attempts")
            break
        elif guess < secret_number:
            print("Too low. Try a higher number.")
        else:
            print("Too high. Try a lower number.")

    if attempts == max_attempts:
        print(f"Oops, you have ran out of attempts. The correct number is {secret_number}. Better luck next time")
    
    play_again = input("Do you want to play again, [y] or [n]: ").lower()

    if play_again == "y":
        continue
    elif play_again == "n":
        print("Hope you enjoyed.")
        break
    else:
        print("Unexpected ERROR!!!!.")
        break

