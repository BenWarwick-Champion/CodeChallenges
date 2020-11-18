# https://www.hackerrank.com/challenges/apple-and-orange/problem?h_r=next-challenge&h_v=zen


# My solution
def count_applesandoranges(s, t, a, b, apples, oranges):
    apple_counter, orange_counter = 0, 0
    for apple in apples:
        if (a + apple) >= s and (a + apple) <= t:
            apple_counter += 1
    for orange in oranges:
        if (b + orange) >= s and (b + orange) <= t:
            orange_counter += 1

    print(apple_counter)
    print(orange_counter)


# Ultra pythonic solution -- navjotahuja92 (Hackerrank)
def count_applesandoranges2(s, t, a, b, apples, oranges):
    print(sum([1 for x in apples if (x + a) >= s and (x + a) <= t]))
    print(sum([1 for x in oranges if (x + b) >= s and (x + b) <= t]))


# This is boilerplate input code from HackerRank
if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    count_applesandoranges(s, t, a, b, apples, oranges)
