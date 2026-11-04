print("Welcom to Casino")

answer =input("Do you wanna play ; yes or no              ")

if answer ==("yes"):
    number=int(input("Choose on number between 1~30"))
else:
    print("Bye")

import random

money = random.randint(1, 31)

if number == money:
    print("u win",money)
else:
    print("you lose",money)
