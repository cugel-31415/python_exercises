num1 = int(input("Number please: "))
num2 = int(input("Number please: "))
num3 = int(input("Number please: "))
num4 = int(input("Number please: "))

largest = num1
for num in [num2, num3, num4]:
    if num > largest:
        largest = num

print("The largest number is", largest)

