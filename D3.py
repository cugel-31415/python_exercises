def list_2_str(lst):
    str1 = "".join(lst)
    return str1


lst1 = ['O', 'K', 'I', 'D', 'O']
lst2 = ['K', 'I']
lst_all = [lst1, lst2]

for lst in lst_all:
    if len(lst) != 5:
        print("This was not what we agreed upon. I said it could be only 5 characters long, remember? I can't let you do that.")
    else:
        print("Alright. Here is your string: ", list_2_str(lst))

