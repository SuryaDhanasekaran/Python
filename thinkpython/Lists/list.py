# cheeses = ['Cheddar','Edam','Gouda']
# numbers = [42,123]
# empty = []
# print(cheeses,numbers,empty)

#List are Mutable

# numbers = [42,123]
# numbers[1] = 5
# print(numbers)

# cheeses = ['Cheddar','Edam','Gouda']
# print('Edam' in cheeses)

#TRAVERSING A LIST

# cheeses = ['Cheddar','Edam','Gouda']

# for cheese in cheeses:
#     print(cheese)

# numbers = [1,2,3,4,5]
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2
# print(numbers)

#FOR LOOP OVER AN EMPTY LIST NEVER RUNS THE BODY

# for x in []:
#     print('This never happens')

# LIST OPERATIONS

# a = [1,2,3]
# b = [4,5,6]
# c = a + b
# print(c)

#THE * OPERATOR REPEATS A LIST A GIVEN NUMBER OF TIMES

# a = [0] * 4
# print(a)
# b = [1,2,3] * 3
# print(b)

# LIST SLICES

# t = ['a','b','c','d','e','f']
# print(t[1:3])
# print(t[:4])
# print(t[3:])
# print(t[:])

#A slice operator on the left side of an assignment can update multiple elements
# t = ['a','b','c','d','e','f']
# t[1:3] = ['x','y']
# print(t)