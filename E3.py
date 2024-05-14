my_lst1 = [6,2,7,4,3]
my_lst2 = ['a', 'b', 'c', 1, 2, 3, 4, 'd', 5, "hello"]
lsts = [my_lst1, my_lst2]

for lst in lsts:
    half_len = len(lst) // 2
    tuple1 = tuple(lst[:half_len])
    tuple2 = tuple(lst[half_len:half_len * 2])
    print("Tuple 1 is:", tuple1)
    print("Tuple 2 is:", tuple2)

for lst in lsts:
    tuple1 = tuple(lst[::2])
    tuple2 = tuple(lst[1::2])
    print("Tuple 1 is:", tuple1)
    print("Tuple 2 is:", tuple2)

