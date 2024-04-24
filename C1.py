letter = input("Please, would you be so kind as to provide me with a letter from the English alphabet? Just type it in after the prompt and press <ENTER>. Thank you su much. ")
print()

letter_uc = letter[0:1].upper()
vowels = "AEIOU"
consonants = "BCDFGHJKLMNPQRSTVWXYZ"
if letter_uc in vowels:
    print("This is a vowel")
elif letter_uc in consonants:
    print("This is a consonant")
else:
    print("I think there was a misunderstanding. Maybe my instructions were not clear enough. Please try again and read the instructions carefully.")

print("\n\n")