# Write a piece of code to determine whether
# a number is a palindrome.

def palindrome_checker(input):
    workStr = str(input)
    for i in range(int(len(workStr)/2)):
        if workStr[i] != workStr[-(i + 1)]:
            return False
    return True

if __name__ == "__main__":
    inputNumber = 1234554321
    if palindrome_checker(inputNumber):
        print("Number is a palindrome")
    else:
        print("Not a palindrome")