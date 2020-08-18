# The maximum sum subarray problem consists in finding the maximum sum 
# of a contiguous subsequence in an array or list of integers:

# max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]


# My Solution
def max_sequence(arr):
    sum, maxSum = 0, 0
    for i in arr:
        sum += i
        if sum < 0:
            sum = 0
        elif sum > maxSum:
            maxSum = sum
    return maxSum

# Best Solution
def max_sequence(arr):
    best_sum = 0
    current_sum = 0
    for x in numbers:
        current_sum = max(0, current_sum + x)
        best_sum = max(best_sum, current_sum)
    return best_sum