import datetime
PASSWORD = "1234"    
def check_password():
    pwd = input("Enter password: ")
    if pwd == PASSWORD:
        return True
    else:
        print("Wrong password ")
        return False
def write_entry():
    entry = input("Write your secret entry:\n")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open("diary.txt", "a") as file:
        file.write("\n" + date + "\n")
        file.write(entry + "\n")

    print("Entry saved ")
def read_entries():
    try:
        with open("diary.txt","r") as file:
            print("\n--- Your Secret Diary ---")
            print(file.read())
    except FileNotFoundError:
        print("No diary entries yet.")
def main():
    print("Welcome to Secret Diary")

    if not check_password():
        return

    while True:
        print("\n1. Write new entry")
        print("2. Read diary")
        print("3. Exit")

        choice = input("Choose (1-3): ")

        if choice == "1":
            write_entry()
        elif choice == "2":
            read_entries()
        elif choice == "3":
            print("Diary closed,goodbye!")
            break
        else:
            print("Invalid choice")
main()
S
