my_lst1 = [2, 2, 3, 3, 4]
my_lst2 = [7, 7, 2, 2, 3]
lsts = [my_lst1, my_lst2]

for lst in lsts:
    avg = 0
    for num in lst:
        avg += num

    print("The average is:", avg / len(lst))    


for lst in lsts:
    avg = 0
    for num in lst:
        avg += num

    print("The average was:", avg / len(lst))
    to_add = (len(lst) + 1) * 5 - avg
    lst.append(to_add)
    print("Added {}, new list is {}".format(to_add, lst))   
    print("The average is now 5")