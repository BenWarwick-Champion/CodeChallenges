# You are given an array (which will have a length of at least 3, but could be very large)
# containing integers. 
# The array is either entirely comprised of odd integers or entirely comprised of even 
# integers except for a single integer N. 
# Write a method that takes the array as an argument and returns this "outlier" N.

# Example:
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)

# My Solution
def find_outlier(integers):
    even = []
    odd = []
    for integer in integers:
        if (integer % 2) == 0:
            even.append(integer)
        else:
            odd.append(integer)
    
    if len(even) < len(odd):
        return even[0]
    return odd[0]

# Best Solution
def find_outlier(int):
    odds = [x for x in int if x%2!=0]
    evens= [x for x in int if x%2==0]
    return odds[0] if len(odds)<len(evens) else evens[0]