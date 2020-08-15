# Given n, take the sum of the digits of n. 
# If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# This is only applicable to the natural numbers.

# My Solution
def digital_root(n):
    
    if n < 10:
        return n
    
    sum = 0
    numString = str(n)
    
    for x in numString:
        sum += int(x)

    return digital_root(sum)


# Best Solution
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))