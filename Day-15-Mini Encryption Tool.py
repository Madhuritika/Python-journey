def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base=ord('A') if char.isupper() else ord('a')
            result+=chr((ord(char) - base + shift) % 26 + base)
        else:
            result+=char
    return result
def decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char
    return result
print("MINI ENCRYPTION TOOL")
print("1.Encrypt")
print("2.Decrypt")
choice = input("Choose(1/2): ")
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))
if choice== "1":
    encrypted = encrypt(message, shift)
    print("Encrypted Message:", encrypted)
elif choice == "2":
    decrypted = decrypt(message, shift)
    print("Decrypted Message:", decrypted)
else:
    print("Invalid choice")
