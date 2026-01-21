import random
secret_number=random.randint(1, 20)
attempts=0
print("I have chosen a number between 1 and 20.")
print("Try to guess it!")
while True:
    guess=int(input("Enter your guess: "))
    attempts += 1
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Yeah! You're the champion !")
        print("You guessed it in", attempts, "attempts.")
        break
