import random
user_score = 0
computer_score = 0
choices = ["rock", "paper", "scissors"]
print("Welcome to Rock Paper Scissors Game!")
while True:
    print("\nChoose one:")
    print("rock")
    print("paper")
    print("scissors")
    print("exit")
    user_choice=input("Your choice: ").lower()
    if user_choice=="exit":
        print("\nGame Over!")
        print("Your score:", user_score)
        print("Computer score:", computer_score)
        break
    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue
    computer_choice=random.choice(choices)
    print("Computer chose:", computer_choice)
    if user_choice==computer_choice:
        print("It's a tie!")
    elif user_choice=="rock" and computer_choice == "scissors":
        print("You win!")
        user_score += 1
    elif user_choice=="paper" and computer_choice == "rock":
        print("You win!")
        user_score += 1
    elif user_choice=="scissors" and computer_choice == "paper":
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1


