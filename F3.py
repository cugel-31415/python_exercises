red_set = {"Tomato", "Apple", "Brick", "Pepper", "Cap", "Strawberry", "Berry"}
fruit_set = {"Mango", "Banana", "Apple", "Grape", "Kiwi", "Strawberry", "Orange", "Berry", "Tangerine"}
red_fruits = set()
non_red_fruits = set()

for fruit in fruit_set:
    red = False
    for red_object in red_set:
        if fruit == red_object:
            red_fruits.add(fruit)
            red = True

    if not red:
        non_red_fruits.add(fruit)

print(red_fruits)
print(non_red_fruits)

orange_set = {"King's Day T-Shirt", "Orange", "Pumpkin", "Tangerine", "Carrot", "Pillow", "Earthenware Pot"}
red_or_orange_fruits = set()
objects = red_set
objects |= orange_set

for fruit in fruit_set:
    red = False
    orange = False
    for red_object in red_set:
        if fruit == red_object:
            red_or_orange_fruits.add(fruit)
            red = True

    if not red:
        for orange_object in orange_set:
            if fruit == orange_object:
                red_or_orange_fruits.add(fruit)
                orange = True

    if fruit in objects:
        objects.remove(fruit)


print(red_or_orange_fruits)
print(objects)

all_objects = orange_set
all_objects |= red_set
all_objects |= fruit_set

print(list(all_objects))