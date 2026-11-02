import random

answer = random.randint(1, 100)
tries = 0

while True:
    guess = int(input("Guess a number from 1 to 100: "))
    tries = tries + 1

    if guess < answer:
        print("higher")
    elif guess > answer:
        print("lower")
    else:
        print("Correct!")
        print("Number of tries:", tries)
        break