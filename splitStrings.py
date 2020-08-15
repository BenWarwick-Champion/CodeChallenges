# Complete the solution so that it splits the string into pairs of two characters. 
# If the string contains an odd number of characters then it should replace 
# the missing second character of the final pair with an underscore ('_').

# Example:
# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

# My Solution
def solution(s):
    if (len(s) % 2) != 0:
        s += '_'
    return [s[i:i+2] for i in range (0, len(s), 2)]


# Best Solution
import re

def solution(s):
    return re.findall(".{2}", s + "_")