my_dict1 = {0: 19, 1: 33, 2: 18, 3: 30, 4: 26}
my_dict2 = {0: 45, 1: 7, 2: 44, 3: 81, 4: 6}
my_dicts = [my_dict1, my_dict2]

for dict in my_dicts:
    lst = []
    for key in dict.keys():
        lst.append(dict[key])

    lst.sort()

    index = 0
    for key in dict.keys():
        dict[key] = lst[index]
        index += 1

    print("The sorted dictionary is:", dict)