# https://www.hackerrank.com/challenges/kangaroo/problem

# My solution
def kangaroo(x1, v1, x2, v2):
    if (v1 <= v2) or ((x2 - x1)%(v1 - v2) != 0):
        return 'NO'
    return 'YES'

# If you have forgotten how to do this the trick was
# to treat the kangaroos as two lines and look for
# intersections. (y=mx+c and then equate)
# Result from the final equation needs to be a
# positive integer in order to meet the test criteria