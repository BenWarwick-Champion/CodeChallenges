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


if __name__ == "__main__":
    input_number = input('Enter the range: ')

    sieve_primes(int(input_number))

#