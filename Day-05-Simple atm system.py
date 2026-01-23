balance=int(input("Enter initial balance: "))
while True:
    print("\nMenu:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Choose an option (1-4): ")
    
    if choice == '1':
        amount = float(input("Enter deposit amount: "))
        if amount > 0:
            balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid amount. Please enter a positive number.")
    
    elif choice == '2':
        amount = float(input("Enter withdrawal amount: "))
        if 0 < amount <= balance:
            balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Invalid amount. Please enter a positive number not exceeding your balance.")
    
    elif choice == '3':
        print(f"Current balance: {balance}")
    
    elif choice == '4':
        print("Exiting the program.")
        break
    
    else:
        print("Invalid choice. Please select a valid option.")
