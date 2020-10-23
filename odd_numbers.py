import time

# Prints every odd number up to the input value
def odd_numbers(n):
    for i in range(1, n, 2):
        print(i)

# Prints every odd number up to the input value
def odd_numbers_alt(n):
    for i in range(1, n):
        if i%2 != 0:
            print(i)

if __name__ == "__main__":
    n = 100 # Sets the input value
    start1 = time.perf_counter()
    odd_numbers(n)
    end1 = time.perf_counter()
    start2 = time.perf_counter()
    odd_numbers_alt(n)
    end2 = time.perf_counter()
    time1 = end1 - start1
    time2 = end2 - start2
    print('Process 1 completed in: ', time1)
    print('Process 2 completed in: ', time2)