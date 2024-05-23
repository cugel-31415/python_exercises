coordinates = (34.0522, -118.2437)
print(coordinates[0])
print(coordinates[1])

student = {"name" : "Alice", "age" : 24, "courses" : ["Math", "Science", "English"]}
student.update({"graduated" : False})
student["age"] = 25
print(student)

unique_numbers = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1}
unique_numbers.add(6)
unique_numbers.remove(2)
if 3 in unique_numbers:
    print("3 is in unique_numbers")
else:
    print("3 is not in unique_numbers")
