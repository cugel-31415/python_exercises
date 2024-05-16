my_dict1 = {0: 19, 1: 33, 2: 18, 3: 30, 4: 26}
my_dict2 = {}
my_dicts = [my_dict1, my_dict2]

for dict in my_dicts:
    if len(dict) > 0:
        print("This dictionary is not empty")
    else:
        print("This dictionary is empty")
