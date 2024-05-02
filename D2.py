def mutilate_list(lst):
    lst.sort()
    lst.pop(0)
    lst.pop(len(lst) - 1)
    return lst


lst1 = [34, 1, 0, 65, 28, 127, 345]
lst2 = [7, 98, 55, 3, 1259, 31]
lst_all = [lst1, lst2]

for lst in lst_all:
    print("Look! I improved your list! Here it is: ", mutilate_list(lst))

print("Are you happy or are you happy?")