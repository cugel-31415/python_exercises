tuple_1 = (1,2,3)
tuple_2 = (4,5,6)
tuple_3 = (2,3,7,4)
tuple_4 = (7,1)
tuple_pairs = [[tuple_1, tuple_2], [tuple_3, tuple_4]]

for pair in tuple_pairs:
    new_tuple = pair[0] 
    new_tuple += pair[1]
    print("The new tuple is:", new_tuple)

