password_length = int(input("Enter the password length: "))
import random
import string
all_characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(all_characters) for _ in range(password_length))
print("Generated password:", password)
