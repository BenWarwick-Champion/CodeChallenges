# Program to find happy numbers


def is_happy(num):
    seen = set()
    while(num != 1):
        num = sum(int(i)**2 for i in str(num))
        if num in seen:
            return False
        seen.add(num)
    return True

if __name__ == "__main__":
    number = input('Input number to check happiness: ')
    if (is_happy(number)):
        print('That\'s a happy number!')
    else:
        print('You need to cheer up your number...')