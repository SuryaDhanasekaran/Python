# Given an array of integers, find the sum of its elements.

# Examples:

# Input : arr[] = {1, 2, 3}
# Output : 6
# Explanation: 1 + 2 + 3 = 6
# This Python program calculates the sum of an array by iterating through each element and adding it to a running total. The sum is then returned. An example usage is provided to demonstrate the calculation of the sum for a given array.




list1 = [12, 3, 4, 15]
s=0
for i,a in enumerate(list1): 
  s+=a 
print(s)