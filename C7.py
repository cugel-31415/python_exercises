passed = False
if int(input("What is 2 * 2? ")) == 4:
    print("That is correct!")
    if int(input("What is 6 / 3? ")) == 2:
        print("That is also correct!")
        answer = int(input("What is 9 * 9? "))
        if  answer == 18 or answer == 81:
            passed = True

if passed:
    print("Correct! You passed the test!")
else:
    print("That is false. You failed the test!")
