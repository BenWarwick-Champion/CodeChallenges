# Write a program to iteratively create the fibonacci sequence

def iterative_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    for index, n in zip(range(100), iterative_fibonacci()):
        print(index, n)

    # Method to just print the nth value from the generator
    for index, n in enumerate(iterative_fibonacci()):
        if index == 10:
            print(n)
            