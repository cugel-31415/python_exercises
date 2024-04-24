num1 = int(input("Number please: "))
num2 = int(input("Number please: "))
num3 = int(input("Number please: "))

sum = num1 + num2 + num3
same = num1 == num2 and num1 == num3

if same:
    print("These numbers are the same!")
print("The sum of these numbers is", sum)
if same:
    print("Multiplied by 4 this becomes", 4 * sum)


