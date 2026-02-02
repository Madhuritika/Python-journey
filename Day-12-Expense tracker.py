expenses = []

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        expenses.append((name, amount))
        print("Expense added successfully!")

    elif choice == "2":
        if expenses:
            print("\nYour Expenses:")
            for item in expenses:
                print(item[0], ":", item[1])
        else:
            print("No expenses recorded yet.")

    elif choice == "3":
        total = 0
        for item in expenses:
            total += item[1]
        print("Total amount spent:", total)

    elif choice == "4":
        print("Exiting Expense Tracker. Bye!")
        break

    else:
        print("Invalid choice. Try again.")
