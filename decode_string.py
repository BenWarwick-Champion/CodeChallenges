# JPMorgan Decode String Question

# A message containing a string of digits needs to be decoded:
# the key is:
# 1 -> A
# 2 -> B
# ...
# 26 -> Z
# Given a non-empty string containing only digits,
# determine the total number of ways to decode it.
# ABCDEFGHIJKLMNOPQRSTUVWXYZ

# Reference for future Ben: (Old: 21/11/20)
# Iterate backwards through the input string
# Look at the last two digits
# If the 2nd last digit is 0 then the last increments count
# If it is 1 then the count must be incremented by 2
# If it is 2 then and the last digit is 0-7 then count+2


# This method doesn't work in it's current state
def decode_num(str, ind, count):
    # Trying to create a base case for the problem
    if ind == 0:
        if str[ind] != '0':
            count += 1
        return count

    # If it's a 0 then the two numbers need to be
    # treated as a pair and only 1 is added to the
    # number of permutations.
    # (This doesn't account for erroneous digits
    # like 30, 40, 50 etc)
    if str[ind] == '0':
        count += 1
        decode_num(str, ind - 2, count)
    else:
        # Now we're looking for the 'teens' values
        if str[ind-1] == '1':
            count += 1
            decode_num(str, ind - 1, count)
        
        # Now trying to capture 21-26
        if str[ind-1] == '2' and int(str[ind]) < 7:
            count += 1
            decode_num(str, ind - 1, count)
        else:
            count += 1
            decode_num(str, ind - 1, count)

# Obviously I'm not doing a very good job of recursing
# the function calls end up returning null values because
# despite reaching the correct value for this test case
# it then tries to execute the remaining code rather than
# breaking from the function at the base case.



# This solution works.
# It came from the leetcode forums, credit to StefanPochmann
# who of course was able to do it in one line (Python2 though):

# from functools import reduce
# def numDecodings_oneliner(s):
#     return reduce(lambda(v,w,p),d:(w,(d>'0')*w+(9<int(p+d)<27)*v,d),s,(0,s>'',''))[1]*1

# More readable version of the above function
def numDecodings(s):
    """
    :type s: str
    :rtype: int
    """
    previous_number_of_ways = 0
    number_of_ways = int(s > '')
    previous_digit = ''

    for digit in s:
        copy_previous = previous_number_of_ways
        previous_number_of_ways = number_of_ways

        # check if the current digit is greater than zero
        # If it is, then (digit>'0') becomes true,
        # and we multiply that by the total number of ways so far
        # ...Think permutations
        number_of_ways = (digit > '0')*number_of_ways

        # At the same time, we check if the current digit and the next digit, are less than 27..
        # If they are, then its another permutation possibility
        # Again, we are checking the truth,
        # and multiplying it by the number of previously known was,
        # not the current number of ways
        #
        # We have the 9< check because if the digit we are on is a zero, then we won't count the
        # next permutation
        number_of_ways += (9 < int(previous_digit+digit) < 27)*copy_previous

        # Finally, remember that our last digit was the digit we are on now
        previous_digit = digit

    return number_of_ways


if __name__ == "__main__":
    inputString = '123'
    expectedAnswer = 3  # ABC, LC, AW

    # 1234:   ABCD, LCD, AWD
    # 12:2, 226:3, 0:0

    if numDecodings(inputString) == expectedAnswer:
        print("Correct")
    else:
        print("Wrong")
        print("Output: ", numDecodings(inputString))
        print("Expected: ", expectedAnswer)
