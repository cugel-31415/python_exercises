# This is a terribly unjust tax system
# someone who earns 67001 euro pays thousands of euro's more in taxes than someone who earns 2 euros less

income = int(input("What is your income in euros? (This information will be processed anonimously, if you are lucky) "))

if income > 97000:
    tax = income * 34 / 100
elif income > 67000:
    tax = income * 31 / 100
else:    
    tax = income * 24 / 100

print("Your income after taxes is {} euros".format(income - tax))


