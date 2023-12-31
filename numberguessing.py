import random

print("WELCOME TO YOUR NUMBER GUESSING GAME!!!!!")

lower_limit = 0
upper_limit = 30
secret_number = random.randint(lower_limit, upper_limit)

attempts = 0
max_attempts = 15

while attempts < max_attempts:
    guess = int(input(f"What is your guess? Choose from between {lower_limit} and {upper_limit}: "))
    attempts += 1

    if guess == secret_number:
        print(f"Congrats, You have guessed it correctly")
        break
    elif secret_number >= 15:
        print("You're near, its either 15 or more than it")
    else:
        print("Its below 15")

if attempts == max_attempts:
    print(f"Oops, you have ran out of attempts. The correct number is {secret_number}")