# Given a list, write a Python program to swap first and last element of the list.

# Examples: 

# Input : [12, 35, 9, 56, 24]
# Output : [24, 35, 9, 56, 12]

# Input : [1, 2, 3]
# Output : [3, 2, 1]

def interchange_first_last(lst):

    if len(lst)>=2:
        lst = lst[-1:] + lst[1:-1] + lst[0:1]
        return lst

iplst = [12,21]
result = interchange_first_last(iplst)
print(result)

