# input = [[1,2],[3,4],[5,6]]

# output = [1,2,3,4,5,6]

input = [[1,2],[3,4],[5,6]]
from itertools import chain
output = chain.from_iterable(input)
print(list(output))
    