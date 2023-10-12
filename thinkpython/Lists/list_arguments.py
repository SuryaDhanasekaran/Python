# def delete_head(t):
#     del t[0]

# letters = ['a','b','c']
# delete_head(letters)
# print(letters)

#APPEND METHOD MODIFIES THE LIST BUT THE + OPERATOR CREATES A NEW LIST

# t1 = [1,2]
# t2 = t1.append(3)
# print(t1)

# t1 = [1,2,3]
# t3 = t1 + [4] #+ operator create a new list and leaves the original list unchanged
# print(t1)
# print(t3)
# print(t1)

# def bad_delete_head(t):
#     t = t[1:]
# t4 = [1,2,3]
# bad_delete_head(t4)
# print(t4)

# def tail(t):
#     return t[1:]
# letters = ['a','b','c']
# rest = tail(letters)
# print(rest)