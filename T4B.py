integers = []
for num in range(1, 16):
    integers.append(num)

div_by_3 = False
div_by_5 = False
for num in integers:
    div_by_3 = False
    div_by_5 = False
    
    if num % 3 == 0:
        div_by_3 = True
    if num % 5 == 0:
        div_by_5 = True

    if div_by_3 and div_by_5:
        print("FizzBuzz")
    elif div_by_3:
        print("Fizz")
    elif div_by_5:
        print("Buzz")
    else:
        print(num)


