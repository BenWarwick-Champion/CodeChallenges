# Write a piece of code to create a fibonacci sequence using recursion

def recursive_fibonacci(n):
    if n > 1:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
    return n

if __name__ == "__main__":
    for i in range(20):
        print(i, recursive_fibonacci(i))
