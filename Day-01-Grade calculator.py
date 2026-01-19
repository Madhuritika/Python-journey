#Grade calculator
A simple yet practical Python program that calculates letter grades based on numerical marks. This was one of my early Python projects to understand conditional logic.
Features
- Takes user input for marks
- Uses `if-elif-else` logic for decision making
- Covers all grade ranges from F to A+
- Clear and beginner friendly code

#Code
marks=int(input("Enter your marks: "))
if marks<50:
    print("F")
elif marks>=50 and marks<60:
    print("D")
elif marks>=60 and marks<70:
    print("C")
elif marks>=70 and marks<80:
    print("B")
elif marks>=80 and marks<90:
    print("A")
else:
    print("A+")
