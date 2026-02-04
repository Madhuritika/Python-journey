text = input("Enter a sentence: ")
char_count = len(text)
word_count = len(text.split())
vowels = "aeiouAEIOU"
vowel_count = 0
for ch in text:
    if ch in vowels:
        vowel_count += 1
digit_count = 0
for ch in text:
    if ch.isdigit():
        digit_count += 1
reversed_text = text[::-1]
print("\n--- Text Analysis Result ---")
print("Characters:", char_count)
print("Words:",word_count)
print("Vowels:",vowel_count)
print("Digits:",digit_count)
print("Reversed text:",reversed_text)
