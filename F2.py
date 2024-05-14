my_dict1 = {"dad": "Eise", "sister_1": "Iris", "sister_2": "Nicky"}
key1 = "dad"
my_dict2 = {"fruit": "Apple", "vegetable":"Capsicum"}
key2 = "meat"

items = [(my_dict1, key1), (my_dict2, key2)]

for item in items:
    dict = item[0]
    search_key = item[1]
    found = False
    for key in dict.keys():
        if key == search_key:
            found = True
            break
    
    result = " "
    if not found:
        result = " not "
    
    print("{} is{}in the dictionary".format(search_key, result))

    if not found:
        dict |= {search_key : "empty"}
        print("The new dictionary is:", dict)


