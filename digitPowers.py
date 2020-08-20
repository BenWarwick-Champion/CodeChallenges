# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p
# we want to find a positive integer k, if it exists, 
# such as the sum of the digits of n taken to the successive powers of p is equal to k * n.

# In other words:
# Is there an integer k such as : (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k
# If it is the case we will return k, if not return -1.

# Note: n and p will always be given as strictly positive integers.

# My Solution
def dig_pow(n, p):
    sum = 0
    nString = str(n)
    
    for index, digit in enumerate(nString):
        sum += int(digit)**(p+index)
        
    if sum % n == 0:
        return sum // n
    return -1

# Best Solution
def dig_pow(n, p):
  s = 0
  for i,c in enumerate(str(n)):
     s += pow(int(c),p+i)
  return s/n if s%n==0 else -1
  