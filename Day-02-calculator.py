num_1=int(input("Enter the first number: "))
num_2=int(input("Enter the second number: "))
operation=input("Enter the operation (+, -, *, /, %, //): ") 
if operation=='+':
    answer=num_1 + num_2
    print("the answer is: ", answer)
elif operation=='-':
    answer=num_1 - num_2
    print("the answer is: ", answer)
elif operation=='*':
    answer=num_1 * num_2
    print("the answer is: ", answer)
elif operation=='/':
    if num_2 == 0:
        print("Error: Division by zero is not allowed")
    else:
        answer = num_1 / num_2
        print("The answer is:", answer)
elif operation=='%':
    answer=num_1 % num_2
    print("the answer is: ", answer)
elif operation=='//':
    answer=num_1 // num_2
    print("the answer is: ", answer)
else:
    print("Invalid operation")
