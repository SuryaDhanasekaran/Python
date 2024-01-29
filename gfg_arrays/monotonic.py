# Given an array A containing n integers. The task is to check whether the array is Monotonic or not. An array is monotonic if it is either monotone increasing or monotone decreasing. An array A is monotone increasing if for all i <= j, A[i] <= A[j]. 

# An array A is monotone decreasing if for all i <= j, A[i] >= A[j]. 

# Return Type: Boolean value, “True” if the given array A is monotonic else return “False” (without quotes). 

# Examples:

# Input : 6 5 4 4
# Output : true

# Input : 5 15 20 10
# Output : false



def isMonotonic(A):
    x, y = [], []
    x.extend(A)
    y.extend(A)
    x.sort()
    y.sort(reverse=True)
    if(x == A or y == A):
        return True
    return False
 
A = [6, 5, 4, 4]
print(isMonotonic(A))