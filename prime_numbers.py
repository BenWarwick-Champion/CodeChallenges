# Print out all prime numbers up to 100
import math

# First simplistic iteration
def simple_primes(num):
    prime = True
    for i in range(2, num):
        if (num % i == 0):
            prime = False
    if (prime):
        print(num)

# Pythonic version
def pythonic_primes1(num):
    if all(num % i != 0 for i in range(2, num)):
        print(num)

# only checking 2 to sqrt(num)
def pythonic_primes2(num):
    if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
        print(num)

# The real optimum implementation - Sieving
def sieve_primes(num):
    sieve = [True] * (num + 1)
    for prime in range(2, num + 1):
        if (sieve[prime]):
            print(prime)
            for i in range(prime, num + 1, prime):
                sieve[i] = False

# Iterative version of prime generation
def gen_primes():
# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
    D = {}
    q = 2
    while True:
        if q not in D:
            yield q
            D[q * q] = [q]
        else:
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1

if __name__ == "__main__":
    input_number = input('Enter the range: ')
    sieve_primes(int(input_number))
    print("------End Sequence------")

    for index, n in zip(range(100), gen_primes()):
        print(index, n)
