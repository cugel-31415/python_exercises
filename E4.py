tuples = [(3, 4), (8, 13), (-5, 34), (-16, -45), (1011, 89)]

lst = []
for tpl in tuples:
    lst.append([tpl[1], tpl])

lst.sort()
for item in lst:
    print(item[1])

