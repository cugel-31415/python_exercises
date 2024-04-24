str = input("Gimme some nonsense: ")
str_len = len(str)
if str_len >= 5:
    # this does not work for some reason. can't find it in the course material either. pretty sure there was an example in class
    # but try to find that in a 3 hour video that is soooooooo slow to navigate through.
    str = 't'.join(str.split())
elif str_len == 4 or str_len == 2:
    str = str[::-1]
elif str_len == 3:
    str = str[2] + str[:2]
else:
    str = 6 * str

print(str)

