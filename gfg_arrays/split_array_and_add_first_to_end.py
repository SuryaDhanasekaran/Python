# Input : arr[] = {12, 10, 5, 6, 52, 36}
#             k = 2
# Output : arr[] = {5, 6, 52, 36, 12, 10}
# Explanation : Split from index 2 and first 
# part {12, 10} add to the end .


arr = [12, 10, 5, 6, 52, 36]
n = len(arr)
position = 2
x = arr[:position]
y = arr[position:]
y.extend(x)
for i in y:
    print(i, end=" ")