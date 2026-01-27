print("Enter your name:")
name = input()
score = 0
print("Hello, " + name + "!")
print("It's quiz time!")
print("Type A, B, C or D\n")
print("1. What is the capital of France?")
print("A) Berlin")  
print("B) Madrid")
print("C) Paris")   
print("D) Rome")
if input().upper() == "C":
    print("Correct!\n")
    score = score + 1
else:
    print("Wrong! The correct answer is C) Paris\n")
print("2. What is 2 + 2?")
print("A) 3")   
print("B) 4")
print("C) 5")
print("D) 22")
if input().upper() == "B":
    print("Correct!\n")
    score = score + 1
else:
    print("Wrong! The correct answer is B) 4\n")
print("3. Which planet is known as the Red Planet?")
print("A) Earth")
print("B) Mars")
print("C) Jupiter")
print("D) Saturn")
if input().upper() == "B":
    print("Correct!\n")
    score = score + 1
else:
    print("Wrong! The correct answer is B) Mars\n")
  
print("Your final score is: " + str(score) + " out of 3",name + "!")
