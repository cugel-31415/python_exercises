set_1 = [1, 2, 3, 4]
set_2 = [7, 8, 9, 10]
set_3 = ["one", "two", "three", "four"]
set_4 = [1, 2, 3, 4]
set_pairs = [(set_1, set_2), (set_3, set_4)]

for pair in set_pairs:
    dict = {}
    set_len = len(pair[0])
    if set_len == len(pair[1]):
        for i in range(set_len):
            dict |= {pair[0][i] : pair[1][i]}

    print("The dictionary is:", dict)

