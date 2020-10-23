# Solutions to the classic FizzBuzz problem
# numbers 1-100 must be printed out
# multiples of 3 are replaced with 'Fizz'
# multiples of 5 are replaced with 'Buzz'
# multiples of both 3 and 5 are replaced with 'FizzBuzz'

# A more typical implementation
def FizzBuzz():
    for i in range(1, 101):
        if (i%3 == 0) and (i%5 == 0):
            print('FizzBuzz')
        elif i%3 == 0:
            print('Fizz')
        elif i%5 == 0:
            print('Buzz')
        else:
            print(i)

# A more pythonic approach
def Compact_FizzBuzz():
    for i in range(1, 101):
        print('Fizz'*(i%3==0)+'Buzz'*(i%5==0) or i)

if __name__ == "__main__":
    Compact_FizzBuzz()