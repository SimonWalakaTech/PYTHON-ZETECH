import random

win = random.randint(1, 50)

guess = int(input("enter guess"))

print(win)
if guess == win:
    print("YOU HAVE WON")
elif guess < win:
    print("TOO LOW")
elif guess > win:
    print("TOO HIGH")


