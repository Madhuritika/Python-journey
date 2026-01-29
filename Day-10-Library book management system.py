library = []

while True:
    print("\n--- Library Management System ---")
    print("1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice =="1":
        book = input("Enter book name to add: ")
        library.append(book)
        print("Book added successfully!")
    elif choice =="2":
        if library:
            print("\nBooks in Library:")
            for book in library:
                print("-", book)
        else:
            print("No books available in the library.")
    elif choice =="3":
        book = input("Enter book name to borrow: ")
        if book in library:
            library.remove(book)
            print("You borrowed the book:", book)
        else:
            print("Book not found.")
    elif choice =="4":
        book = input("Enter book name to return: ")
        library.append(book)
        print("Book returned successfully!")
    elif choice =="5":
        print("Exiting Library System. Bye!")
        break
    else:
        print("Invalid choice. Please try again.")
