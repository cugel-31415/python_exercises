def check_list(lst):
    if type(lst) == list:
        return len(lst)
    else:
        return -1
    

lst1 = []
lst2 = [1, 2, 3, 4]
lst3 = "Ah, hello."
lst_lst = [lst1, lst2, lst3]

for lst in lst_lst:
    if check_list(lst) > 0:
        print("The list is not empty.")
    elif check_list(lst) == 0:
        print("The list is empty.")
    else:
        print("Dude, this is not a list.")
