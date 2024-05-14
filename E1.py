my_lst1 = [1,2,3,4,5,6]
my_lst2 = [1,2,3]
my_lsts = [my_lst1, my_lst2]

for lst in my_lsts:
    if len(lst) >= 4:
        lst.pop(3)
    if len(lst) >= 3:
        lst.pop(2)
    if len(lst) >= 1:
        lst.pop(0)
    print(lst)
