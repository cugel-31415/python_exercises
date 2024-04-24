num = int(input("Would you be so kind as to enter a number between 100 and 999: "))

print()
print()

if num < 100 or num > 999:
    print("What aspect of this simple question did you not understand?")
    print("I'm asking this in order for us to be able to improve our services.")
    print("After the beep you will have an opportunity to leave your comments.")
    print("Thank you.")
    print("Beep")
else:
    num_str = str(num)
    num_str_len = len(num_str)
    reverse_str = ""
    for i in range(num_str_len):
        reverse_str += num_str[num_str_len - i - 1]

    print("For your convenience we have reversed this number and now it has become", reverse_str)


print()
print()

   